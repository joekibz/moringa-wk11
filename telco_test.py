
##<----------------------------------------
#Telco billing pipeline unittesting
##----------------------------------------->

import pandas as pd
import unittest
import telco_pipe




##<-----------------------------
#Unit Tests class declaration
##------------------------------>

class TestDataPipeline(unittest.TestCase):

    def setUp(self):
    
        """
            Setup initial test data
        """
        self.test_data = pd.DataFrame({
            'customer_id': [1, 2, 3, 4, 5],
            'billing_amount': ['$1000', '$2000', '$3000', '$4000', '$5000'],
            'tax_amount': [100, 200, 300, 400, 500],
            'total_charges' : [1100, 2200, 3300, 4400, 5500]
        })


    def test_data_extraction(self):
        """
        Test the function: data_extraction
        """
        # Test case 1: Verify if data is extracted correctly
        data = telco_pipe.data_extraction('test_data.csv')
        self.assertEqual(len(data), 5, "Incorrect number of rows extracted")
        self.assertListEqual(
            list(data.columns),
            ['customer_id', 'billing_amount', 'tax_amount'],
            "Incorrect column names extracted"
        )
        self.assertListEqual(
            [str(dtype) for dtype in data.dtypes],
            ['int64', 'object', 'int64'],
            "Incorrect column types extracted"
        )

        # Test case 2: Verify if an empty DataFrame is returned for an empty CSV file
        data = telco_pipe.data_extraction('empty_data.csv')
        self.assertEqual(len(data), 0, "Non-empty DataFrame extracted from empty CSV file")
        self.assertListEqual(
            list(data.columns),
            ['customer_id', 'billing_amount', 'tax_amount'],
            "Incorrect column names extracted from empty CSV file"
        )

        # Test case 3: Verify if an exception is raised for a non-existent file
        with self.assertRaises(FileNotFoundError, msg="No exception raised for non-existent file"):
            data = telco_pipe.data_extraction('nonexistent_file.csv')

    
    def test_data_transformation(self):
        """
        Test the function: data_transformation
        """
        # Test case 1: Verify if duplicates are dropped
        transformed_data = telco_pipe.data_transformation(self.test_data)
        self.assertEqual(len(transformed_data), 5, "Task 1: Incorrect number of rows after dropping duplicates")

        # Test case 2: Verify if billing_amount is converted to float and $ is removed
        expected_billing_amount = [1000.00, 2000.00, 3000.00, 4000.00, 5000.00]
        self.assertListEqual(
            list(transformed_data['billing_amount']),
            expected_billing_amount,
            "Task 2: Incorrect billing_amount values after conversion"
        )

        # Test case 3: Verify if total_charges is calculated correctly
        expected_total_charges = [1100, 2200, 3300, 4400, 5500]
        self.assertListEqual(
            list(transformed_data['total_charges']),
            expected_total_charges,
            "Task 3: Incorrect total_charges values after calculation"
        )


    def test_data_loading(self):
        """
        Test the function: data_loading
        """
        # Test case 1: Verify if data is saved to the output file correctly
        output_file = 'output.csv'
        telco_pipe.data_loading(self.test_data, output_file)
        loaded_data = pd.read_csv(output_file)
        self.assertTrue(
            loaded_data.equals(self.test_data),
            "Task 1: Incorrect data saved to the output file"
        )

        # Test case 2: Verify if the output file has the expected column order
        expected_columns = ['customer_id', 'billing_amount', 'tax_amount', 'total_charges']
        loaded_data_columns = list(loaded_data.columns)
        self.assertListEqual(
            loaded_data_columns,
            expected_columns,
            "Task 2: Incorrect column order in the output file"
        )


    def tearDown(self):
        # Clean up any resources if needed
        pass



if __name__ == '__main__':
    
    ##Run the methods defined in TestDataPipeline class and report on results of testing
    unittest.main()
