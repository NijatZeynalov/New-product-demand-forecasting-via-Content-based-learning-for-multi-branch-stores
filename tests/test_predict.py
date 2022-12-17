import pytest
from modeling.content_filtering import ContentRecommender

input_row = ['fəlsəfə', 'Qanun', 'yumşaq', 'Əyyar Cəfərli', 345, 'ingilis dili', 'Platonla 90 dəqiqə', 8.9, 'qbedii']

class TestInputData:

    def test_input_len(self):
        assert len(input_row)==9, "incorrect number of the paramaters."

    def test_input_datatypes(self):
        assert type(input_row[4])==int, "incorrect datatype for sehife_sayi, must be int."
        assert type(input_row[7]) == float, "incorrect datatype for qiymet, must be float."