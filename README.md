# csbom cli tool

This is a cli tool that parses an SBOM outputted by Scribe Security valint tool, formatted as CycloneDX, and creates a csv file containing the following.

### Installation

**Notice:** the tool is still in development, therefore it is suggested not to install it directly to your PATH. Instead, you could create a virtual python environment using python's [virtualenv](https://virtualenv.pypa.io/en/latest/installation.html) tool.

With this tool, you can create an environment with the command `virtualenv <env_name>`. virtualenv will create a directory in your current directory named `<env_name>`.

To activate your environment, on Linux/Mac you can run `source <env_name>/bin/activate` and on windows, `.\env_name\Scripts\activate`

To exit the environment, run `deactivate` and your terminal should go back to normal.

While in the venv, do this to install (this way, the tool will only be installed in the virtual environment):

Using the python package manager, run
```
pip install -i https://test.pypi.org/simple/ csbom==0.0.7
```

Example of installing and running csbom in a virtual environment:
```shell
# Create a virtual environment named `venv`
$ virtualenv venv
created virtual environment CPython3.10.10.final.0-64 in 159ms
  creator CPython3Posix(dest=<dest_path>, clear=False, no_vcs_ignore=False, global=False)
  seeder FromAppData(download=False, pip=bundle, setuptools=bundle, wheel=bundle, via=copy, app_data_dir=<app_dir> Application Support/virtualenv)
    added seed packages: pip==23.2.1, setuptools==68.0.0, wheel==0.41.0
  activators BashActivator,CShellActivator,FishActivator,NushellActivator,PowerShellActivator,PythonActivator

# Activate the virtual environment
$ source venv/bin/activate

# Install csbom tool
(venv) $ pip install -i https://test.pypi.org/simple/ csbom==0.0.7
Looking in indexes: https://test.pypi.org/simple/
Collecting csbom==0.0.7
  Obtaining dependency information for csbom==0.0.7 from https://test-files.pythonhosted.org/packages/24/ed/c46dd8429296ef7a4cb41125f6a1b44f942b4acb18097fb5f61f97fc1170/csbom-0.0.4-py3-none-any.whl.metadata
  Downloading https://test-files.pythonhosted.org/packages/24/ed/c46dd8429296ef7a4cb41125f6a1b44f942b4acb18097fb5f61f97fc1170/csbom-0.0.4-py3-none-any.whl.metadata (360 bytes)
Collecting click>=7.1.2 (from csbom==0.0.7)
  Obtaining dependency information for click>=7.1.2 from https://test-files.pythonhosted.org/packages/1a/70/e63223f8116931d365993d4a6b7ef653a4d920b41d03de7c59499962821f/click-8.1.6-py3-none-any.whl.metadata
  Using cached https://test-files.pythonhosted.org/packages/1a/70/e63223f8116931d365993d4a6b7ef653a4d920b41d03de7c59499962821f/click-8.1.6-py3-none-any.whl.metadata (3.0 kB)
Downloading https://test-files.pythonhosted.org/packages/24/ed/c46dd8429296ef7a4cb41125f6a1b44f942b4acb18097fb5f61f97fc1170/csbom-0.0.4-py3-none-any.whl (7.9 kB)
Using cached https://test-files.pythonhosted.org/packages/1a/70/e63223f8116931d365993d4a6b7ef653a4d920b41d03de7c59499962821f/click-8.1.6-py3-none-any.whl (97 kB)
Installing collected packages: click, csbom
Successfully installed click-8.1.6 csbom-0.0.7

# Now, you can run csbom in your virtual environment!
(venv) $ which csbom
.../venv/bin/csbom

# Using the csbom tool
(venv) $ csbom dep2table bom.json -o analysis.csv
Dependency table successfully generated at `analysis.csv`!

# To exit the virtual environment
(venv) $ deactivate

# Notice that the (venv) disappears after calling deactivate
$ exit

```

The tool can still be installed and run normally without a virtual environment, this is just an example for how to install it exclusively in a virtual environment.

### Usage & Explanations

`csbom CMD [OPTIONS] ARG`

**General Options**:  \
--help: display help information  \
-o (--output): Choose output filename (default `dep/file/commit-analysis.csv`, depending on command)  \
-a (--append-to):  Optional, if present, csbom will append the output to the already existing csv specified  \

**Commands**:  \
dep2table: Given an SBOM generated with the '--components files' flag, output a table of important info,  \
file2table: Given an SBOM as the argument, outputs a table of components of type file,  \
git2table: Given an SBOM generated from a Git repo (with --components commits), outputs a table with all commit information,  \
version: displays current version

**file2table**  \
This command takes the SBOM and generates a CSV with 5 columns,
`bomref`, `name`, `hash`, `mimetime`, `mode`, and `last_commit`
Each row contains an entry from the `components` array in the SBOM file with the corresponding information. If a component does not contain an entry for any of these 5 categories, it will be marked as None

**dep2table**  \
This command creates a CSV table of depender components mapped to dependee components, with information of `name`, `type`, `purl`, `hashes`, and `group` for each component.

**git2table**  \
This command creates a CSV table of git commits with 6 columns, `bomref`, `type` (which should always be commit), `name`, `commit-author`, `commit-message`, and `commit-timestamp`, for each commit in the SBOM.

**version**
displays the current version information
