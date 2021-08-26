# Importing Modules
import os
import shutil
import time

# Function: Main
def main():

	# Initialize
	deleted_folders_count = 0
	deleted_files_count = 0

	# Path
	path = "/PATH_TO_DELETE"

	# Days
	days = 30

	# Convert the Days to Seconds
	seconds = time.time() - (days * 24 * 60 * 60)

	# Check if the file is present or not
	if os.path.exists(path):
		# Iterating all folders/files
		for root_folder, folders, files in os.walk(path):
			# Comparing Days
			if seconds >= get_file_or_folder_age(root_folder):
				# Remove Folder
				remove_folder(root_folder)
				deleted_folders_count += 1
				break
			else:
				# Check Folder
				for folder in folders:
					# Path of the Folder
					folder_path = os.path.join(root_folder, folder)
					# Compare with days
					if seconds >= get_file_or_folder_age(folder_path):
						# Remove Folder
						remove_folder(folder_path)
						deleted_folders_count += 1
				# Check current directory files
				for file in files:
					# Path of File
					file_path = os.path.join(root_folder, file)
					# Compare days
					if seconds >= get_file_or_folder_age(file_path):
						# Remove File
						remove_file(file_path)
						deleted_files_count += 1
		else:
			# If the path mentioned is not in a directory
			if seconds >= get_file_or_folder_age(path):
				remove_file(path)
				deleted_files_count += 1 # incrementing count
	else:
		# If folder is not found
		print(f'"{path}" is not found')
		deleted_files_count += 1
	print(f"Total folders deleted: {deleted_folders_count}")
	print(f"Total files deleted: {deleted_files_count}")

# Function
def remove_folder(path):
	# Remove folder
	if not shutil.rmtree(path):
		# Message: Success
		print(f"{path} is removed successfully")
	else:
		# Message: Fail
		print(f"Unable to delete the "+path)

# Function
def remove_file(path):
	# Remove File
	if not os.remove(path):
		# Message: Success
		print(f"{path} is removed successfully")
	else:
		# Message: Fail
		print("Unable to delete the "+path)

# Function
def get_file_or_folder_age(path):
	# Get time
	ctime = os.stat(path).st_ctime
	# Return
	return ctime

if __name__ == '__main__':
	main()