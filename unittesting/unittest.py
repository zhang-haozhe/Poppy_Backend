import unittest
import modules.text_processor
import modules.image_processor
import modules.create_event
import instruction_set
import log_file_set
import incomplete_img_set
import img_set

class TestBackendMethods(unittest.TestCase):

    def test_create_event(self):
        self.assertEqual(create_event.times_per_day(instruction1), 'numPlaceHolder1')
        self.assertEqual(create_event.times_per_day(instruction2), 'numPlaceHolder2')
        self.assertEqual(create_event.times_per_day(instruction3), 'numPlaceHolder3')

        self.assertEqual(create_event.create_log_file(instruction1, 1), 'logFile1')
        self.assertEqual(create_event.create_log_file(instruction2, 1), 'logFile2')
        self.assertEqual(create_event.create_log_file(instruction3, 1), 'logFile3')

    def test_image_processor(self):
        self.assertEqual(image_processor.resize(incImg1), img1)
        self.assertEqual(image_processor.resize(incompImg2), img2)
        self.assertEqual(image_processor.resize(incImg3), img3)

    def test_text_processor(self):
       self.assertEqual(text_processor.removes_whitespace(instruction1), 'whitespace_cleaned_instruction1')
       self.assertEqual(text_processor.removes_whitespace(instruction2), 'whitespace_cleaned_instruction2')

       self.assertEqual(text_processor.correct_instruction(instruction1), 'correctedInstruction1')
       self.assertEqual(text_processor.correct_instruction(instruction1), 'correctedInstruction2')
       

if __name__ == '__main__':
    unittest.main()