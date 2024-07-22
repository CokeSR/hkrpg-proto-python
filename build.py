import os
import subprocess

script_dir = os.path.dirname(os.path.abspath(__file__))
proto_folder = os.path.join(script_dir, "proto", "hkrpg")
output_folder = os.path.join(script_dir, "output")
protoc = os.path.join(script_dir, "srv", "bin", "protoc.exe")

def convert(proto_folder, output_folder, protoc):
    for root, dirs, files in os.walk(proto_folder):
        for file in files:
            if file.endswith(".proto"):
                proto_path = os.path.join(root, file)
                output_file = file.replace(".proto", "_pb2.py")
                output_path = os.path.join(output_folder, output_file)
                command = [protoc, f"--python_out={output_folder}", f"--proto_path={proto_folder}", proto_path]
                subprocess.run(command, check=True)

if __name__ == "__main__":
    convert(proto_folder, output_folder, protoc)
    print("Operation done.")
