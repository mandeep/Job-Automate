from click.testing import CliRunner
import jobautomate.commandline


class TestJobAutomate:

    def test_indeed_api_parameters(self):
        parameters = jobautomate.commandline.indeed_parameters('Financial Analyst', 'New York City')
        assert isinstance(parameters, dict) is True
        assert 'Financial Analyst' in parameters.values()
        assert 'New York City' in parameters.values()

    def test_indeed_api_urls(self):
        parameters = jobautomate.commandline.indeed_parameters('Financial Analyst', 'New York City')
        job_urls = jobautomate.commandline.indeed_urls(parameters)
        assert len(job_urls) > 1
        for url in job_urls:
            assert 'http://' in url

    def test_indeed_apply_button(self, selenium):
        selenium.get(
            "http://www.indeed.com/cmp/Discover-Books/jobs/Full-Time-Driver-3ce56851d8772139")
        selenium.implicitly_wait(7)
        jobautomate.commandline.find_apply_button(selenium, 'indeed-apply-button')

    def test_fill_application(self, selenium):
        selenium.get(
            "http://www.indeed.com/cmp/Discover-Books/jobs/Full-Time-Driver-3ce56851d8772139")
        selenium.implicitly_wait(7)
        jobautomate.commandline.find_apply_button(selenium, 'indeed-apply-button')
        jobautomate.commandline.switch_frames(selenium, 'iframe[name$=modal-iframe]')
        jobautomate.commandline.fill_application(
            selenium, 'Homer', 'Simpson', 'Chunkylover53@aol.com', 'resume.txt')

    def test_fill_application_again(self, selenium):
        selenium.get(
            "http://www.indeed.com/viewjob?jk=b2eb45e8bccc4861")
        selenium.implicitly_wait(7)
        jobautomate.commandline.find_apply_button(selenium, 'indeed-apply-button')

        jobautomate.commandline.switch_frames(selenium, 'iframe[name$=modal-iframe]')
        jobautomate.commandline.fill_application(
            selenium, 'Homer', 'Simpson', 'Chunkylover53@aol.com', 'resume.txt')

    def test_click_apply(self, selenium):
        selenium.get(
            "http://www.indeed.com/cmp/Discover-Books/jobs/Full-Time-Driver-3ce56851d8772139")
        selenium.implicitly_wait(7)
        jobautomate.commandline.find_apply_button(selenium, 'indeed-apply-button')
        jobautomate.commandline.switch_frames(selenium, 'iframe[name$=modal-iframe]')
        jobautomate.commandline.fill_application(
            selenium, 'Homer', 'Simpson', 'Chunkylover53@aol.com', 'resume.txt')
        jobautomate.commandline.apply_or_continue(selenium, debug=True)

    def test_click_apply_again(self, selenium):
        selenium.get(
            "http://www.indeed.com/viewjob?jk=b2eb45e8bccc4861")
        selenium.implicitly_wait(7)
        jobautomate.commandline.find_apply_button(selenium, 'indeed-apply-button')

        jobautomate.commandline.switch_frames(selenium, 'iframe[name$=modal-iframe]')
        jobautomate.commandline.fill_application(
            selenium, 'Homer', 'Simpson', 'Chunkylover53@aol.com', 'resume.txt')
        jobautomate.commandline.apply_or_continue(selenium, debug=True)

    def test_cli_command(self):
        runner = CliRunner()
        result = runner.invoke(
            jobautomate.commandline.cli, ['--debug', 'Homer', 'Simpson', 'Chunkylover53@aol.com',
                                          'Nuclear Technician', '.travis.yml'], input='No')
        assert not result.exception
        verbose_result = runner.invoke(
            jobautomate.commandline.cli, ['--debug', '--verbose', 'Homer', 'Simpson',
                                          'Chunkylover53@aol.com', 'Nuclear Technician',
                                          '.travis.yml'], input='No')
        assert not verbose_result.exception

        continue_result = runner.invoke(
            jobautomate.commandline.cli, ['--debug', 'Homer', 'Simpson', 'Chunkylover53@aol.com',
                                          'Nuclear Technician', '.travis.yml'], input='Yes')
        assert not continue_result.exception
