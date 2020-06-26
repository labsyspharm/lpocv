from setuptools import setup, find_packages
import versioneer

def main():
    setup(name='lpocv',
          version=versioneer.get_version(),
          description= 'Leave-pair-out cross-validation',
          long_descriptioni=(
            'Python module that implements leave-pair-out',
            'cross-validation for regression problems.',
            'Allows the user to include errors on the regression labels and'
            'allows to match the samples by subtype (groups)'
                            ),
          author='Mauli Nariya',
          author_email='mauliknariya@gmail.com',
          url='http://github.com/mauliknariya/lpocv',
          packages=find_packages(),
          install_requires=['numpy', 'scikit_learn', 'itertools'],
          cmdclass=versioneer.get_cmdclass(),
          keywords=['leave-pair-out', 'cross-validation', 
                    'batch effects', 'bioinformatics'],
          classifiers=[
            'Development Status :: 1 - Alpha',
            'Intended Audience :: Science/Research',
            'License :: OSI approved :: MIT License',
            'Operating System :: OS Independent',
            'Programming Language :: Python :: 3',
            'Topic :: Scientific/Engineering :: Bio-Informatics']
         
         )
if __name__=='__main__':
    main()
