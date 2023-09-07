from django.test import TestCase
from django.test import TestCase
from json.decoder import JSONDecodeError
from rest_framework.test import RequestsClient
from rest_framework import status

# Create your tests here.
HOST = 'http://localhost:8000'
MOVIES_ENDPOINT = HOST +'/movies/'
RATINGS_ENDPOINT= HOST + '/ratings/'

movie_payload = {
'title': 'Happy Family'
}

def get_movie_endpoint (movie_id):
    return HOST + '/movies/%d/'% movie_id

class CreateMovieTestCase(TestCase):
    def setUp(self):
        self.client = RequestsClient()
        
    def test_with_valid_payload(self):
        r = self.client.post(MOVIES_ENDPOINT,data=movie_payload)
        self.assertEqual(r.status_code,status.HTTP_201_CREATED)
        data= r.json()
        expected_movie = {
            'id': 1,
            'title': movie_payload ['title'],
            'rating': None,
            }
        self.assertEqual (data, expected_movie)
        
class AddRatingTestCase(TestCase):
    def setUp(self):
        self.client =RequestsClient()
        try:
            self.movie= self.client.post(MOVIES_ENDPOINT,data=movie_payload).json()
        except JSONDecodeError:
            self.fail('Implement correct POST method for the endpoint')
            
    def test_with_existing_movie(self):
        rating_payload = {
            'movie': self.movie['id'],
            'value': 4,
        }
        r = self.client.post(RATINGS_ENDPOINT, data=rating_payload)
        self.assertEqual(r.status_code, status.HTTP_201_CREATED)

        data = r.json()
        expected_rating = {
                'id': 1,
                'movie': self.movie['id'],
                'value': 4,
        }
        self.assertEqual(data,expected_rating)
    def test_with_rating_smaller_than_allowed_minimum(self):
        rating_payload = {
                'movie': 1,
                'value': 0,
        }
        r = self.client.post(RATINGS_ENDPOINT, data=rating_payload)
        self.assertEqual(r.status_code, status.HTTP_400_BAD_REQUEST)
    def test_with_rating_greater_than_allowed_maximum(self):
        rating_payload={
            'movie': 1,
            'value': 6,
        }
        r = self.client.post(RATINGS_ENDPOINT, data=rating_payload)
        self.assertEqual(r.status_code, status.HTTP_400_BAD_REQUEST)
    def test_with_non_existing_movie(self):
        rating_payload = {
        'movie': 2,
        'value': 4,
        }
        r = self.client.post(RATINGS_ENDPOINT, data=rating_payload)
        self.assertEqual(r.status_code, status. HTTP_400_BAD_REQUEST)
        
class GetMovieTestCase(TestCase):
    def setUp(self):
        self.client = RequestsClient()
        try:
            self.movie = self.client.post(MOVIES_ENDPOINT, data=movie_payload).json()
        except JSONDecodeError:
            self.fail('Implement correct POST method for the endpoint')
            
    def test_with_no_ratings(self):
        url = get_movie_endpoint(self.movie['id'])
        r = self.client.get(url)
        self.assertEqual(r.status_code, status.HTTP_200_OK)
        data = r.json()
        expected_movie = {
            'id': self.movie['id'],
            'title': movie_payload ['title'],
            'rating': None,
            }
        self.assertEqual (data, expected_movie)
        
    def test_with_two_ratings(self):
        rating_payloads = [
            {'movie': self.movie['id'], 'value': 4},
            {'movie': self.movie['id'], 'value': 5},
        ]
        for payload in rating_payloads:
            self.client.post(RATINGS_ENDPOINT, data=payload)
        url = get_movie_endpoint(self.movie['id'])
        r = self.client.get(url)
        self.assertEqual(r.status_code, status.HTTP_200_OK)
        data=r.json()
        expected_rating = sum(obj ['value'] for obj in rating_payloads) / len(rating_payloads)
        expected_movie = {
            'id':self.movie['id'],
            'title':movie_payload['title'],
            'rating':expected_rating,
            }
        
        self.assertEqual(data, expected_movie)
        
    def test_with_ratings_to_different_movies(self):
        another_movie = self.client.post(MOVIES_ENDPOINT, data={'title': 'Another movie'}).json()
        rating_payloads = [
            {'movie': self.movie['id'], 'value': 2},
            {'movie': another_movie ['id'], 'value': 1},
            {'movie': self.movie['id'], 'value':5},
        ]
        for payload in rating_payloads:
            self.client.post(RATINGS_ENDPOINT, data=payload)
        url = get_movie_endpoint(self.movie['id'])
        r = self.client.get(url)
        self.assertEqual(r.status_code, status.HTTP_200_OK)
        data = r.json()
        sum_expected_ratings = sum(obj ['value'] for obj in rating_payloads
                if obj ['movie'] == self.movie['id'])
        num_expected_ratings = len([obj ['value'] for obj in rating_payloads
                if obj ['movie'] == self.movie['id']])
        expected_movie = {
                'id': self.movie['id'],
                'title': movie_payload ['title'],
                'rating': sum_expected_ratings / num_expected_ratings,
        }
        self.assertEqual(data, expected_movie)
        
    def test_with_non_existing_movie(self):
        url = get_movie_endpoint(2)
        r = self.client.get(url)
        self.assertEqual(r.status_code, status.HTTP_404_NOT_FOUND)

