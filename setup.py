from setuptools import setup

setup(name='galkin',
      version='1.0',
      description='A tool to handle the available data on the rotation curve of the Milky Way.',
      author='Miguel Pato and Fabio Iocco',
      author_email='mailto:galkin.tool.mw@gmail.com',
      url='https://github.com/galkintool/galkin',
      packages=['galkin'],
      package_data={'galkin': ['data/*.dat']},
      scripts=['bin/galkin_data.py','bin/galkin_data_fast.py','bin/galkin_plotter.py','bin/inputpars.txt','bin/output/posdata_baseline.dat','bin/output/vcdata_baseline.dat','bin/output/rawdata_baseline.dat','bin/output/posdata_baseline_gas.dat','bin/output/vcdata_baseline_gas.dat','bin/output/rawdata_baseline_gas.dat','bin/output/posdata_baseline_gas.dat','bin/output/vcdata_baseline_stars.dat','bin/output/rawdata_baseline_stars.dat','bin/output/posdata_baseline_masers.dat','bin/output/vcdata_baseline_masers.dat','bin/output/rawdata_baseline_masers.dat','bin/output/posdata_R85.dat','bin/output/vcdata_R85.dat','bin/output/posdata_R75.dat','bin/output/vcdata_R75.dat'],
)
