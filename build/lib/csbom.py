import click

from app import application

@click.group
@click.option('-o', '--output', default='bom-analysis.csv', help='Intended name for output file')
def csbom(output):
    pass

@csbom.command()
@click.argument('sbom')
@click.option('-o', '--output', default='bom-analysis.csv', show_default=True, help='Intended name for output file')
def file2table(sbom, output):
    """Given an SBOM generated with the '--components files' flag, output a table of important info"""
    if application.__format(sbom):
        application.parse_sbom(sbom, output)
        click.echo(f'File information table successfully generated at \'{output}\'')
    else:
        click.echo('ERROR: This SBOM file is not in CycloneDX format. Please ensure that your SBOM has the proper output format flag when running valint')

@csbom.command()
@click.argument('sbom')
@click.option('-o', '--output', default='dep-analysis.csv', show_default=True, help='Intended name for output file')
def dep2table(sbom, output):
    """Given an SBOM, output a table of dependencies"""
    if application.__format(sbom):
        if application.dependencies(sbom):
            application.parse_dependencies(sbom, output)
            click.echo(f'Dependency table successfully generated at \'{output}\'')
        else:
            click.echo('ERROR: This SBOM file does not contain any dependencies. Please ensure the SBOM has a dependencies array as one of the initial keys in the JSON object.')
    else:
        click.echo('ERROR: This SBOM file is not in CycloneDX format. Please ensure that your SBOM has the proper output format flag when running valint')

@csbom.command()
@click.argument('sbom')
@click.option('-o', '--output', default='commit-analysis.csv', show_default=True, help='Intended name for output file')
def git2table(sbom, output):
    """Given an SBOM generated from a Git repo, outputs a table with all commit information"""
    if application.__format(sbom):
        application.parse_git_data(sbom, output)
        click.echo(f'Git commit table successfully generated at \'{output}\'')
    else:
        click.echo('ERROR: This SBOM file is not in CycloneDX format. Please ensure that your SBOM has the proper output format flag when running valint')

@csbom.command()
def version():
    """Display current version information"""
    click.echo('csbom version (in development): 0.0.6')
