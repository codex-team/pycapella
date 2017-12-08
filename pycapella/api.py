import json
import os.path
import requests
import logging


class CapellaApi:
    """
    Python SDK for Capella
    @Website: https://capella.pics
    @Documentation: https://github.com/codex-team/capella
    """

    def __init__(self, config={}):
        """
        Initialize API_URL
        :param config:
        """
        self.API_URL = config.get("API_URL", "https://capella.pics/upload")

    def uploadUrl(self, url):
        """
        Upload remote URL to Capella
        :param url: URL for uploading to Capella
        :return: False if error or response if success (watch doc for self.processRespose)
        """
        try:
            response = requests.post(self.API_URL, {'link': url})
            return self.processRespose(response)

        except Exception as e:
            logging.error("[uploadUrl runtime error]: {}".format(e))
            return False

    def uploadFile(self, file_path):
        """
        Upload local file to Capella
        :param file_path: local file path for uploading to Capella
        :return: False if error or response if success (watch doc for self.processRespose)
        """
        if not os.path.isfile(file_path):
            logging.error("[uploadFile] file not found: {}".format(file_path))
            return False
        try:
            files = {'file': open(file_path, 'rb')}
            response = requests.post(self.API_URL, files=files)
            return self.processRespose(response)

        except Exception as e:
            logging.error("[uploadFile runtime error]: {}".format(e))
            return False

    def processRespose(self, response):
        """
        Process and return a response from Capella API
        :param python requests.response object
        :return: response: dictionary(
            'success' – True or False (mandatory)
            'message' – Description of the result (mandatory)
            'id' – Image ID from Capella API (optional)
            'url' – Image URL from Capella API (optional)
        )
        """
        if response.status_code != 200:
            logging.error("[uploadUrl] status code {}\nAPI Response: {}".format(response.status_code, response.content))
            return {'success': False, 'message': response.content}
        else:
            api_response = json.loads(response.text)
            if not api_response.get("success"):
                logging.warning("[uploadUrl] API response with error: {}".format(api_response.get("message")))
            else:
                logging.debug("[uploadUrl] API response with success: {}".format(api_response.get("message")))

            return api_response
