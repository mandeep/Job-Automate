from click.testing import CliRunner

import jobautomate.commandline


def test_cli_command():
    """Test the CLI."""
    runner = CliRunner(echo_stdin=True)
    result = runner.invoke(
        jobautomate.commandline.cli, ['--debug', 'Homer', 'Simpson', 'Chunkylover53@aol.com',
                                      'Nuclear Technician', '.travis.yml'], input='no')
    assert not result.exception


def test_cli_false_key():
    """Test the CLI with a false API key."""
    runner = CliRunner(echo_stdin=True)
    result = runner.invoke(
        jobautomate.commandline.cli, ['--debug', '--key', 'FALSEAPIKEY', 'Homer', 'Simpson',
                                      'Chunkylover53@aol.com', 'Nuclear Technician',
                                      '.travis.yml'], input='no')
    assert result.exception


def test_cli_xvfb():
    """Test the CLI with the --xvfb flag."""
    runner = CliRunner(echo_stdin=True)
    xvfb_result = runner.invoke(
        jobautomate.commandline.cli, ['--debug', '--xvfb', 'Homer', 'Simpson',
                                      'Chunkylover53@aol.com', 'Nuclear Technician',
                                      '.travis.yml'], input='no')
    assert not xvfb_result.exception


def test_cli_verbose():
    """Test the CLI with the --verbose flag."""
    runner = CliRunner(echo_stdin=True)
    verbose_result = runner.invoke(
        jobautomate.commandline.cli, ['--debug', '--verbose', 'Homer', 'Simpson',
                                      'Chunkylover53@aol.com', 'Nuclear Technician',
                                      '.travis.yml'], input='no')
    assert not verbose_result.exception
