from app import google
from pprint import pprint
import time

idToken = "eyJhbGciOiJSUzI1NiIsImtpZCI6IjdiODcxMTIzNzU0MjdkNjU3ZjVlMjVjYTAxZDU2NWU1OTJhMjMxZGIiLCJ0eXAiOiJKV1QifQ.eyJuYW1lIjoiRWdnbyBUdiIsInBpY3R1cmUiOiJodHRwczovL2xoMy5nb29nbGV1c2VyY29udGVudC5jb20vYS0vQU9oMTRHZ3NnTDl0aVhTdEZTZGRud3MteXlmUHozVW1DaFhDNVJ0Z0d6UWk9czk2LWMiLCJpc3MiOiJodHRwczovL3NlY3VyZXRva2VuLmdvb2dsZS5jb20vY2hhdC1sZXZrb3ZvIiwiYXVkIjoiY2hhdC1sZXZrb3ZvIiwiYXV0aF90aW1lIjoxNjMyNjQyMDIzLCJ1c2VyX2lkIjoiOWEyWjEyOWx6b1ZKTzBmUlRqc29LZFNQeDNoMiIsInN1YiI6IjlhMloxMjlsem9WSk8wZlJUanNvS2RTUHgzaDIiLCJpYXQiOjE2MzI3MjU4OTUsImV4cCI6MTYzMjcyOTQ5NSwiZW1haWwiOiJ0aXRhbmljc3YyMkBnbWFpbC5jb20iLCJlbWFpbF92ZXJpZmllZCI6dHJ1ZSwiZmlyZWJhc2UiOnsiaWRlbnRpdGllcyI6eyJnb29nbGUuY29tIjpbIjEwODc1ODQxMTQ5ODU4MDEwMTI5OCJdLCJlbWFpbCI6WyJ0aXRhbmljc3YyMkBnbWFpbC5jb20iXX0sInNpZ25faW5fcHJvdmlkZXIiOiJnb29nbGUuY29tIn19.NjHN5Amr8Km76YIlc4aCdwDsR057W1LmkZSR-nmKHz7_et9x2h8wDv_525rrnk5IBsNmkZGtHUC5QBAZqVdPMbmdI5oFucqCO7CKP_sU-hy49i5AWiRLkU7egI1aU880MavyHLhxXG01bxWSCPELcEH5tWg_QVa3p3NlPYhyDQbxWOm6h333dVK__kgZtnPQ7tuDzeQhS6chghzsPkGbhTk39EeSlUAaoHpE9fYV6LMF12P_wqbYzFCpFcVA_SBsltwGm__8lN3K7pgZMMyOytDZCoolDy7aIpC9LeSgp7uKgx-wc3qWQTBrgc-RELdVFh_zZT9p-b_zdmXDsgEShQ"
print(len(idToken))

start = time.time()
pprint(google.is_valid_google_token(idToken))
print(time.time() - start)