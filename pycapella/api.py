import functools
import json
import os.path
import requests
import logging


class CapellaApi:
    """
    Python SDK for Capella
    @Website: https://capella.pics
    @Documentation: https://github.com/codex-team/pycapella
    """

    def __init__(self, config={}):
        """
        Initialize API_URL
        :param config:
        """
        self.API_URL = config.get("API_URL", "https://capella.pics/upload")
        self.filters = []
        self.url = ""

    def upload_url(self, url):
        """
        Upload remote URL to Capella
        :param url: URL for uploading to Capella
        :return: False if error or response if success (watch doc for self.processRespose)
        """
        try:
            response = requests.post(self.API_URL, {'link': url})
            return self.process_respose(response)

        except Exception as e:
            logging.error("[uploadUrl runtime error]: {}".format(e))
            return False

    def upload_file(self, file_path):
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
            return self.process_respose(response)

        except Exception as e:
            logging.error("[uploadFile runtime error]: {}".format(e))
            return False

    def process_respose(self, response):
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
                self.url = api_response['url']
                logging.debug("[uploadUrl] API response with success: {}".format(api_response.get("message")))

            return api_response

    def crop(self, width, height=None):
        """
        Apply crop filter to the image
        :param width: crop width
        :param height: crop height (optional, initially defined as width)
        :return: self
        """
        self.filters.append(('crop', (width, height if height else width)))
        return self

    def resize(self, width, height=None, left=None, top=None):
        """
        Apply resize filter to the image
        :param width: resized image width
        :param height: resized image height (optional, initially defined as width)
        :param left: resized image left (optional)
        :param top: resized image top (optional)
        :return: self
        """
        if left and top:
            self.filters.append(('resize', (width, height if height else width, left, top)))
        else:
            if left or top:
                logging.warning("[resize] You should define both left and top params")

            self.filters.append(('resize', (width, height if height else width)))
        return self

    def pixelize(self, size):
        """
        Apply pixelize filter to the image
        :param size: size
        :return: self
        """
        self.filters.append(('pixelize', size))
        return self

    def clear(self):
        """
        Clear filters
        :return: self
        """
        self.filters.clear()
        return self

    def get_url(self):
        """
        Get url of the final image
        :return: string URL
        """
        url = ''
        for filter, params in self.filters:
            try:
                if filter == "resize" and len(params) == 4:
                    url += '/{}/{}x{}&{},{}'.format(filter, *params)
                elif filter == "pixelize":
                    url += '/{}/{}'.format(filter, params)
                else:
                    url += '/{}/{}x{}'.format(filter, *params)
            except Exception as e:
                logging.error("[upload] error: {}".format(e))

        if not self.url:
            logging.warning("[upload file before applying filters]")
            return None

        return self.url + url
