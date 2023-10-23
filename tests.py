import unittest
from unittest.mock import patch
import requests
from bulkCreateAnimal import bulk_create_animal


class TestBulkCreateAnimal(unittest.TestCase):

    def setUp(self):
        self.api_key = "your_api_key_here"
        self.base_url = "https://api_here.com"

        # Mock the requests library to prevent making actual API calls
        self.mock_requests = unittest.mock.patch.object(requests, "post")
        self.mock_requests.start()

    def tearDown(self):
        self.mock_requests.stop()

    def test_bulk_create_animal_success(self):
        # Create a mock response object
        mock_response = unittest.mock.Mock()
        mock_response.status_code = 201

        # Set the mock response to be returned by the requests library
        self.mock_requests.return_value = mock_response

        # Create a list of animal data for bulk creation
        animal_data_list ={
            "createAnimalRequestDtos": [
                {
                "lineKey": 0,
                "sexKey": 0,
                "generationKey": 0,
                "breedingStatusKey": 0,
                "dietKey": 0,
                "animalStatusKey": 0,
                "exitReasonKey": 0,
                "animalName": "",
                "physicalMarker": "",
                "dateBorn": "2023-10-23T20:06:28.431Z",
                "dateExit": "2023-10-23T20:06:28.431Z",
                "comments": "",
                "owner": "",
                "arrivalDate": "2023-10-23T20:06:28.431Z",
                "animalUseKey": 0,
                "iacucprotocolKey": 0,
                "physicalMarkerTypeKey": 0,
                "materialOriginKey": 0,
                "externalIdentifier": "",
                "microchipIdentifier": "",
                "jobKeys": [
                    0
                ],
                "cohortKeys": [
                    0
                ],
                "housings": [
                    {
                    "housingKey": 0,
                    "dateIn": "",
                    "dateOut": ""
                    }
                ],
                "animalCharacteristics": [
                    {
                    "animalCharacteristicKey": 0,
                    "characteristicValue": ""
                    }
                ],
                "alternatePhysicalID": "",
                "heldFor": "",
                "citesNumber": ""
                }
            ]
            }


        # Call the bulk_create_animal function
        result = bulk_create_animal(self.api_key, self.base_url, animal_data_list)

        # Assert that the function returned the expected message
        self.assertEqual(result, "Animals created successfully")

    def test_bulk_create_animal_failure(self):
        # Create a mock response object
        mock_response = unittest.mock.Mock()
        mock_response.status_code = 400

        # Set the mock response to be returned by the requests library
        self.mock_requests.return_value = mock_response

        # Create a list of animal data for bulk creation
        animal_data_list =  animal_data_list ={
            "createAnimalRequestDtos": [
                {
                "lineKey": 0,
                "sexKey": 0,
                "generationKey": 0,
                "breedingStatusKey": 0,
                "dietKey": 0,
                "citesNumber": ""
                }
            ]
            }

        # Call the bulk_create_animal function
        result = bulk_create_animal(self.api_key, self.base_url, animal_data_list)

        # Assert that the function returned the expected message
        self.assertEqual(result, "Failed to create animals: 400")

    def test_bulk_create_animal_exception(self):
        # Set the requests library to raise an exception
        self.mock_requests.side_effect = Exception("Error")

        # Create a list of animal data for bulk creation
        animal_data_list = {
                "lineKey": 0,
                "citesNumber": ""
                
            }

        # Call the bulk_create_animal function
        result = bulk_create_animal(self.api_key, self.base_url, animal_data_list)

        # Assert that the function returned the expected message
        self.assertEqual(result, "Error: Error")


if __name__ == "__main__":
    unittest.main()
