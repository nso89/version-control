from pathlib import Path
import shutil


SOURCE = Path.home()


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
    
        file = input("Folder: ").strip()
        version_number = input("Version #: ").strip()
        
        validate_parameters(validate = file, parameter = "File Name")
        validate_parameters(validate = version_number, parameter = "Version Number")

        user_folder = SOURCE.joinpath(file)
        file_location_version = user_folder.parent.joinpath(version_number)
    
        print(f"Source: {user_folder}\nDestination: {file_location_version}")
        shutil.copytree(src = user_folder, dst = file_location_version, dirs_exist_ok = False)
    
    except (ValueError, PermissionError, NotADirectoryError, FileExistsError) as e:
        print(e)
    
if __name__ == "__main__":
    main()
