import re
import numpy as np
import pandas as pd
from colorama import Fore
from urllib.parse import urlparse
import pickle
from tld import get_tld

with open("RandomForestURL.pkl", "rb") as file:
    model = pickle.load(file)

df = pd.read_csv("toll_free_numbers.csv")


def process_tld(url):
    try:
        res = get_tld(url, as_object=True, fail_silently=False, fix_protocol=True)
        pri_domain = res.parsed_url.netloc
    except:
        pri_domain = None
    return pri_domain


def abnormal_url(url):
    hostname = urlparse(url).hostname
    hostname = str(hostname)
    match = re.search(hostname, url)
    if match:
        # print match.group()
        return 1
    else:
        # print 'No matching pattern found'
        return 0


def httpSecure(url):
    htp = urlparse(url).scheme
    match = str(htp)
    if match == "https":
        # print match.group()
        return 1
    else:
        # print 'No matching pattern found'
        return 0


def digit_count(url):
    digits = 0
    for i in url:
        if i.isnumeric():
            digits = digits + 1
    return digits


def letter_count(url):
    letters = 0
    for i in url:
        if i.isalpha():
            letters = letters + 1
    return letters


def Shortining_Service(url):
    match = re.search(
        "bit\.ly|goo\.gl|shorte\.st|go2l\.ink|x\.co|ow\.ly|t\.co|tinyurl|tr\.im|is\.gd|cli\.gs|"
        "yfrog\.com|migre\.me|ff\.im|tiny\.cc|url4\.eu|twit\.ac|su\.pr|twurl\.nl|snipurl\.com|"
        "short\.to|BudURL\.com|ping\.fm|post\.ly|Just\.as|bkite\.com|snipr\.com|fic\.kr|loopt\.us|"
        "doiop\.com|short\.ie|kl\.am|wp\.me|rubyurl\.com|om\.ly|to\.ly|bit\.do|t\.co|lnkd\.in|"
        "db\.tt|qr\.ae|adf\.ly|goo\.gl|bitly\.com|cur\.lv|tinyurl\.com|ow\.ly|bit\.ly|ity\.im|"
        "q\.gs|is\.gd|po\.st|bc\.vc|twitthis\.com|u\.to|j\.mp|buzurl\.com|cutt\.us|u\.bb|yourls\.org|"
        "x\.co|prettylinkpro\.com|scrnch\.me|filoops\.info|vzturl\.com|qr\.net|1url\.com|tweez\.me|v\.gd|"
        "tr\.im|link\.zip\.net",
        url,
    )
    if match:
        return 1
    else:
        return 0


def having_ip_address(url):
    match = re.search(
        "(([01]?\\d\\d?|2[0-4]\\d|25[0-5])\\.([01]?\\d\\d?|2[0-4]\\d|25[0-5])\\.([01]?\\d\\d?|2[0-4]\\d|25[0-5])\\."
        "([01]?\\d\\d?|2[0-4]\\d|25[0-5])\\/)|"  # IPv4
        "(([01]?\\d\\d?|2[0-4]\\d|25[0-5])\\.([01]?\\d\\d?|2[0-4]\\d|25[0-5])\\.([01]?\\d\\d?|2[0-4]\\d|25[0-5])\\."
        "([01]?\\d\\d?|2[0-4]\\d|25[0-5])\\/)|"  # IPv4 with port
        "((0x[0-9a-fA-F]{1,2})\\.(0x[0-9a-fA-F]{1,2})\\.(0x[0-9a-fA-F]{1,2})\\.(0x[0-9a-fA-F]{1,2})\\/)"  # IPv4 in hexadecimal
        "(?:[a-fA-F0-9]{1,4}:){7}[a-fA-F0-9]{1,4}|"
        "([0-9]+(?:\.[0-9]+){3}:[0-9]+)|"
        "((?:(?:\d|[01]?\d\d|2[0-4]\d|25[0-5])\.){3}(?:25[0-5]|2[0-4]\d|[01]?\d\d|\d)(?:\/\d{1,2})?)",
        url,
    )  # Ipv6
    if match:
        return 1
    else:
        return 0


def model_based_converter(url):
    url_features = []

    url_features.append(url.count("@"))
    url_features.append(url.count("?"))
    url_features.append(url.count("-"))
    url_features.append(url.count("="))
    url_features.append(url.count("."))
    url_features.append(url.count("#"))
    url_features.append(url.count("%"))
    url_features.append(url.count("+"))
    url_features.append(url.count("$"))
    url_features.append(url.count("!"))
    url_features.append(url.count("*"))
    url_features.append(url.count(","))
    url_features.append(url.count("//"))

    url_features.append(abnormal_url(url))
    url_features.append(httpSecure(url))
    url_features.append(digit_count(url))
    url_features.append(letter_count(url))

    url_features.append(Shortining_Service(url))
    url_features.append(having_ip_address(url))

    return url_features


def predict_url(url):
    rem = {0: "benign", 1: "defacement", 2: "phishing", 3: "malware"}
    features = model_based_converter(url)
    prediction = model.predict([features])
    return rem[prediction[0]]


def predict_phone_number(phone_number):
    if phone_number in df["Toll Free No"]:
        return f"This number is a toll free number for {df[df['Toll Free No'] == phone_number]['Company Name'].values[0]}"
    else:
        return "This number is not present in our toll free number database."
