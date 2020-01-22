import subprocess
import sys

def check_requirements():
    """
        Check installed packages to ensure you can generate histogram. Matplotlib and pandas packages are required
        Parameters: \n
        None \n
        Returns: \n
        True if python instance has got pandas and matplotlib packages installed
    """
    process_output = subprocess.check_output([sys.executable, '-m', 'pip', 'freeze'])
    installed_packages = [r.decode().split('==')[0] for r in process_output.split()]
    if 'pandas' and 'matplotlib' in installed_packages:
        return True
    else:
        print('You don`t have one of required libralies\n'
              'I can`t create histogram\n'
              'Required libralies: \n'
              '->pandas\n'
              '->matplotlib\n')
        return False
