import pygame
from os import walk

def import_folder(path):
    """Import all images from a folder and return as a list"""
    surface_list = []
    
    try:
        for folder_name, sub_folders, img_files in walk(path):
            for image_name in img_files:
                if image_name.endswith(('.png', '.jpg', '.jpeg')):
                    full_path = path + '/' + image_name
                    image_surf = pygame.image.load(full_path).convert_alpha()
                    surface_list.append(image_surf)
    except:
        # If path doesn't exist, return empty list
        pass
    
    return surface_list

def import_folder_dict(path):
    """Import all images from a folder and return as a dictionary"""
    surface_dict = {}
    
    try:
        for folder_name, sub_folders, img_files in walk(path):
            for image_name in img_files:
                if image_name.endswith(('.png', '.jpg', '.jpeg')):
                    full_path = path + '/' + image_name
                    image_surf = pygame.image.load(full_path).convert_alpha()
                    surface_dict[image_name.split('.')[0]] = image_surf
    except:
        # If path doesn't exist, return empty dict
        pass
            
    return surface_dict

def import_character_assets(path):
    """Import character animation assets organized by state and direction"""
    character_dict = {}
    
    try:
        for folder_name, sub_folders, img_files in walk(path):
            if sub_folders:  # If there are subfolders (like idle_right, run_left, etc.)
                for sub_folder in sub_folders:
                    sub_path = f"{path}/{sub_folder}"
                    character_dict[sub_folder] = import_folder(sub_path)
    except:
        pass
    
    return character_dict
