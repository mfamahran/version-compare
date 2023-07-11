from typer.testing import CliRunner

from src import cli

test_map = [
    {
        'version1': '1.2',
        'version2': '1.2.9.9.9.9',
        'output': "-1"
    },
    {
        'version1': '1.3',
        'version2': '1.3.4',
        'output': "-1"
    },
    {
        'version1': '1.10',
        'version2': '1.3.4',
        'output': "1"
    },
    {
        'version1': '1.1',
        'version2': '1.1',
        'output': "0"
    }
]

runner = CliRunner()

def test_version():
    for test in test_map:
        result = runner.invoke(cli.app, ["compare", "--version1", test.get('version1'), "--version2", test.get('version2')])
        assert result.exit_code == 0
        assert test.get('output') in result.stdout