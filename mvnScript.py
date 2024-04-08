import subprocess


mvn_path = "C:/apache-maven-3.9./bin/mvn.cmd"

def run_mvn_clean_install(directory):
    try:
        subprocess.run([mvn_path, "clean", "install"], check=True, cwd=directory)
        print("mvn clean install completed successfully.")
    except subprocess.CalledProcessError as e:
        print("mvn clean install failed:", e)

def run_mvn_clean_package(directory):
    try:
        subprocess.run([mvn_path, "clean", "package"], check=True, cwd=directory)
        print("mvn clean package completed successfully.")
    except subprocess.CalledProcessError as e:
        print("mvn clean package failed:", e)

# Example usage:
clean_install_list = ['../jogayjoga.auth','../jogayjoga.account','../jogayjoga.court']
clean_package_list = ['../jogayjoga.auth-resource','../jogayjoga.account-resource','../jogayjoga.court-resource','../jogayjoga.discovery','../jogayjoga.gateway']

for directory in clean_install_list:
    run_mvn_clean_install(directory)
for directory in clean_package_list:
    run_mvn_clean_package(directory)

