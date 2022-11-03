from pathlib import Path
import shutil

def validate_parameters(validate: str, parameter: str) -> None:
    """
    Verify if validate is blank, if so, raise ValueError 
    indicating the parameter cannot be blank.
    
    Args:
    validate: str - the string we're checking.
    parameter: str - what validate represents.
    
    Returns:
    None
    """
    if not validate:
        raise ValueError(f"{parameter} cannot be blank!")

def main():

    try:
    
        source = Path.home()
        file = input("Folder: ")
        version_number = input("Version #: ")
    
        validate_parameters(validate = file, parameter = "File Name")
        validate_parameters(validate = version_number, parameter = "Version Number")

        user_folder = source.joinpath(file)
        file_location_version = user_folder.parent.joinpath(version_number)
    
        print(f"Copying {user_folder} to {file_location_version}")
        shutil.copytree(src = user_folder, dst = file_location_version)
    
    except (ValueError, PermissionError, NotADirectoryError) as e:
        print(e)
    
if __name__ == "__main__":
    main()
