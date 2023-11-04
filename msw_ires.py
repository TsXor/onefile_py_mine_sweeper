import base64

RES_INLINE = {

    'img/0.gif': base64.b64decode(
        b'iVBORw0KGgoAAAANSUhEUgAAACQAAAAkCAYAAADhAJiYAAAACXBIWXMAABJ0AAASdAHeZh94AAADx0lE'
        b'QVRYha1Y0W4cIQycYZFStX1o/qD90PxuHqLeY6qmSpg+gI2B5ZpTinS6ZfHi8TA27PLh4UECQBIAABIA'
        b'QbJegmAcjy2MC+Fxtb7U7svvSd22jhAgkNKBX8/PyJJQBAClO2D4gRAB2mwkhD6rpADOvYRreddMfbj5'
        b'EAgISBAymUAId3ef8PnrF5AAmdyH+WGLxGkIQOiWgqDWPyXT7YoEFQEJgBLSceDPy29kpgSUgm/39/jx'
        b'4zuYElJbLrJDilhw4nBsgcHNfUCVXQIVFXG5XJABwjTElCoI/9XoyUpplxFXTLLg7QKNrYknoi05QTZb'
        b'EmDCcRzItsJMBBP9uYnstn7G1k7g9b9iOl86NDBmFwlITMhdCpZdcDF3DGPGITLVnPRMo2ca+l+w7Gqb'
        b'M5eJyN6hiXiUso15bwo6asoXqnsdwJm9Abes7X4GQFHIse4EBFE6c3SRjZBNWoJo2tH5HMklMiDtBpE5'
        b'V9AwEb0kdIY7Mo7xhDmwNhLJwqq6sSc4TR4m2OleHLoj4E2hICLKxhAASK52mnOGqKco14jnG3N+jZ7n'
        b'XI0+MoBeh04d74tgqHG1mg1VkK3CDeTNlXLwQxLJ9qIu5q3/DTbBxKtlbOJwVbhn2cAQBKSTbeIsC25r'
        b'K8SdiZWCZJ0qajsscOP9VkgzO/tx01GqK6YTs9v5+BCD7dILYz3nrFl0zdX7AFTmTdi1XHLYhKNtMnQE'
        b'EZVJ2X3H+6E2l4idIpqGumdTkd4jyFvb2ZRTxGkHlYzC/k/ghiofBBGONfUEFCvcdqKPgNps1HMy0zTU'
        b'jgxxuTRlwMc5mpdizWwy7GXV63wCHpW0q8fnLdpee2bcrXN3ZM9qMhZE1qxD25d8u9lDsQs/N58C8aNa'
        b'm49961gmQ9sw/aDFRUqO/cpqyEGtQIZb7blMCFJpD2uKeqgFZ4e8NYorw2OhDcy5gVod0vy6gv7qG24s'
        b'YLYnr3WunRkdUXXoxw8DNmpxhjRRcYvGBxRqKd+PLuY/rzzM6Nf2Duks47Z1VR1yCU6qb7K5kzClaBNM'
        b'FyXbO97ObS9WHNCMRxBRfZls2oa2lFIZEuQ6osIZd0jb+r+y1gM4Z3RM7YbAczfeKxJypVCASkzuMfYW'
        b'Aam5dk6NfY4TuXULDPq0+VUKcrJXSZX6DcIEx5mNtdTvN29N/RES1TepOMlbeatLllIFRAgJ9gY7y+Cf'
        b'1QTD145dgba1NYaaM4l4fXtFvlx+4uXlBY+PjyhvBTkfOI76s88zbFtzF+u0rOyQztosAudHdVsSM3gc'
        b'eHp6wl+aIaZ9vqBRqAAAAABJRU5ErkJggg=='
    ),

    'img/1.gif': base64.b64decode(
        b'iVBORw0KGgoAAAANSUhEUgAAACQAAAAkCAYAAADhAJiYAAAACXBIWXMAABJ0AAASdAHeZh94AAAH5ElE'
        b'QVRYhV2YzY8kRxHFfy8yu3tnd+218a5BRguSMcbISCAsS4gTQtw48UdwgBs3JE5IHLhysf8CDhxBnCwh'
        b'JIT5XCE4YNlYBvG1Bmy82J71zHRVRnCIzKoa96i6p6uqM+PjxYsXpW99+zthgqKg7grFCqUUzIRkSMIk'
        b'ZAAgBWYCgSQizxL5DwSEAxHggAQhxksy1NdGIlQI7TmbjWl6j7rbiTY3TH2RCCKcCBERCOG5T+6kQATI'
        b'ERAMS4ZR/XeR34UY3ggjIsgVgogAjNlFc2M6n6jCmJpzfb+jHgq7WpGM0p1LU4TIdQWYRT/vuXD/FlqN'
        b'kArFKrVUJCEMqRsU66rjGg4+NWrUHcWD27dvc/PmQxlyAkX6sUlKHgJTUBQ9Pk544AQNiDQdKJgqqPao'
        b'CY8gnPyM9DBdBcN49/4Z1eoO5okmJ7rF1r3XWF49QjIkKHJMDu4Jle5lIQhBqGDaUVRARiDcQW64QOE9'
        b'kh2YIWQFAXVXjLmIYgXrGwIoephxEsPWAR1YT6eW+FneKUOaKbUlXqjgmcbW42aI1kp+6SgE5Xq7QpUM'
        b'hTDLQ71URuA1bhYYLNELz2jsZOz1ALNfww0mn5nOZ4zArh6p0lJ1MtEwDBLQPUqZPWEyKv3i8HgxZvkO'
        b'KKsPHMITL2HMseOF3z7BD3/+cd582zg7g+N54AUOD7zF9772J558/B3M0ruY6dFVAkKZCesVIzPqqGkF'
        b'PQFbIPf3yLwTjUYwBxwRp+/e4IVffJTfvWS50wTMgh1MPMRs18HfQpaQcOt+DUxGGoeEzDDrEfLYGNCt'
        b'XohsqTCHCDycBpyHOP7vAf59fsgbG5c+6wRXD/ep5QLZAXdR1KttoGfZJnJfoEaml+atE0+MW9LA8H4E'
        b'jcbUHNqBR9otfvnaR/jrP5SR8X5MaZTNwZXrR2o94rHLcNDBqNVhYj0lido8Nwv3zswrqBP9lrwkIzzg'
        b'+Ch/+PNT/OAne+785RrtohvS+mfft6hxcpiQFayBD3si28/IQhaSltRVj+Ra720Drc2gUyTImDHun3+I'
        b'7/7oGV58udIc2AEXC9hYKFuw08xJaUClk1PH6ZKE7JGhDVagjvImuiHR2WXc19sAFF586TY/e7nmanM/'
        b'Nk11+XSwOMfsglDvi+Ov97LLrzxjwaDKbIh4bAzb3N9L8q3TAjWdBuA9LuNnHN3iiJmIqR++AebGeGWk'
        b'uhlUlganpXNrQVreFAZRnRvXXuGpR4zHbjmfjr8Tdz/Gc795mKM2+BkHjYIht03wRisefJdp7HmAgMqm'
        b'5LeEaN1EdfVQzPnqM6/yzafvoPke0e4xvf0Vvn/ni7wx3O58Fj7cqqAGFAgthr0/YWu4Ygk+EEvo1s6u'
        b'pbubDNp1op5z1DUuDnvu3Zt5u7ByEJ34AuRB65oo1UDrRukyjiL3oWupGl0SRAeOencRhvX8GoJw1IS1'
        b'CrqCdlc51gM0Jbgbl3BXItiFsOZ4NIiS62/An5Vul4JUh/5JpRhpjPV0hTqBpCfuxtwKcShQG5XApvdF'
        b'vnNroSEc96yybD2DeGORtiN9Wf6iblkn6WCAW7in3AhPzX1U40ITHhe0+YJ5huNYfAtEoO6OTCEs5l65'
        b'KdSWEAWEYpW9BHKn0qOT/WwFZwwM9ahZNEKNSRc0NSbg3YsJ91iaZWwN2htzNIoHikYw4TGomkW/b1UV'
        b'AktBHt2uIbxZ+1qQRsWMdE5EpemCI2dYPQNL8ojCUK4A2HwVpsAdvEykNCs9YxuJwRZ7XYqgITt6Txn8'
        b'EOqGGqKyn8+54o19Cx70Hexa0mthJcyavty6v+fW6YN8gImrh1Nsf8RLQtJjlcjDGvVA1AEojU5Mslx0'
        b'IDelOEeFf77+Ke68ehO34DgZf7x7AtcsK6yLMCy3+P3xIb7+/Od5+PbTXH30Hh/+4CnPPvUmNw6iRg4J'
        b'wimjWZDQqBFrTi+NKFreaMDx4grP3fkcP/7VHg4kMxfgEeCcbCGxGvVOGD+9u4f/3ILdLTiBb3z5Ll/6'
        b'zCtYmTAb810suAP1CLG+BraHDBkKb2bmsG9wo0djyA0nDRznBiY29MIMnMKJ77E2E8aiLOjDKMpTdQij'
        b'xSz1rhZrBk1gO+PqyXtQT3LjI2sjXUZbLvezcb2msQ/fPKWUmdKrMulgwKNARPYy28BnnTY6d/UQHnYT'
        b'X/jEr7l++gTH6YQ6Hwk3PHKSOPYFZw8uJnHuQSsV2+9pO+N6/S+ffOw1DruGRVkdWKg7WbsSvjb2CNRn'
        b'9tFk1TFhLj77JDz7+N+S0dvE7JXZjYgZV0vuCqOE44PtcSjgVVipTLFPBteA3Gjuydx1K8YU0SVmV3Ma'
        b'xJXpPKpCzfkclQ64OXOjIb5aH5Vzx3zI0YdFX5k6G2q8T2YEVZ2kTIMb1Bvq+GEndqnnOwdESi5oDL1X'
        b'iPCcuWL4Pv4PZIaaU22IrBVzodRJyXY4ZmJXRFVQLEfm/vimV0D+OhTLIx8A+SIPN4WVC4P1R0RdjUZ/'
        b'rtRblYbU0YYcTdRoTpTCoYpqPVJaVa+WUknPymZUGgw/kD+uJK11LPaWpF6Og5Gjk/HqcBpa23yk1hOu'
        b'1MqhDjG+mQTG+/IIbQ3J0u4GsW7oY2RkjeGwdKQrVZd61WS3h3r/jX8R1w+8/rq4f3aGlR2l1rWnKT30'
        b'8Fx8M8PFmOlgeXiw9qrMrZQPMUopXYGuHVgYqNJcHKfgnXtn/B8doZYXVTU1CwAAAABJRU5ErkJggg=='
    ),

    'img/10.gif': base64.b64decode(
        b'iVBORw0KGgoAAAANSUhEUgAAACQAAAAkCAYAAADhAJiYAAAACXBIWXMAABJ0AAASdAHeZh94AAAJ0UlE'
        b'QVRYhYWYa4xdVRXHf2vtfe5jpnc6My3SoYVCS8tLy0OF+Ao+kFckCiaoJAqJX/yCYgwJJBqMMSRiCAkq'
        b'xhgUExIDRSnyiAKlhigEkBpRQgnTCrTl0RY6nVfv4+y1/LDPGUaY6k5Ocs+5++z9P3v911r/teSmW37q'
        b'guPm4AnBAMAdd8PdgYTkh6goSHXnTnJwBK+eCQIOIpKv6pnjmDtmYHl5TPK7Awv0k6ICUcXBDcQRnMVD'
        b'ABcHNP+GCowsTBD3Gn+eIUANWiSDXbysOOA4GbS7I5SoBAppETMYUBwzByx/kRtguCVEwKX++mojqRC5'
        b'IA5RBBGtcGZg7p63djAcN8sX5NNyQbUgADboU/Z6xOSCAm6KSgJRgggqms0nAVUhhoJQNImxIIRIjAUx'
        b'BoogOErfDEHBsoEMR8TAHXNw0XwyCyYOOIq55j01IigxT4Dhoskpx61CQ6gM56hWh1B/EUJyxR1EAkgg'
        b'xMhrr7zKY089xTGrV/HB0z+UT9rAvGKQaDZPbdJFI6gC2cSphCiVXU2MEEDEMM92xvJRJ882z1xQIICA'
        b'YSQv2fKHLfz+gYeZWL2Ks245ExPN/LIMIJtQ8rsORgJPqCgqARPH1aGEqOqoCEEl71iTvPKybBDHXSoz'
        b'ZKLiEZVIvw9SNECE3nyXw705Wq3lmdchA0AEQRAJOEZfnHZvhpiE+WaBhICL4kGIeXlZILVSex2ggSKW'
        b'mEX6gxIRB40EjQyIBG0zFBssHx9FJCJEhkaatGMTTwlTBw+IBIKQyevzHLNnO6c+cifG+/jzVTeQXCEo'
        b'wZTo5hDyaVhtF8/eUPQPsfJXv6bsDTGzaggfj6xsdtk1Jdy3fxmqSoqBp5/bjluf+fkpHrr3AY4aW83o'
        b'SJPOWIuJtRvotEeIKhRR8X88yqbHb6f9Wo/u6oJudFrmaACiElVqEBV5ySFALdHuRdbsfJmpA1OMjcCy'
        b'o6DZgC3/hl+8kefWHBXgcK/H7Xf8tnqSve6yCy/huuuvRrwLb73Eugd/STsNoITu8WciEgnBCcGR0omZ'
        b'056pU3PZIbiT2gV7Vh9LcWCK/gCaAqEJj05X0bYOlv81bOGXYxw89DprVhSkuQHh4XsYfnOAD8PcxNHs'
        b'PvtCRnoJWjkDGEZ0rz0gAxF3RBQVpRuUN9qR4RL6b8GOafgX8MT8UkCWHjuf3s6Tn7+SE5rQeesVkoN9'
        b'ehN7vvp1ujqKDvq4CkIEDcTFccEtBzFVMAJ9cSa9wbZZeB3Y1YcDQLmQSFp0xOl7j94RAI0msJ0v8yaw'
        b'F5gVOOriywnNEcLgMK4tSAVaFJQSUPcqDYhUiTI7WU6ngZ1Fh8eBvwNvk6MQgEqHi8cKfnJcj0vGFuW3'
        b'xUNhqII+B0wCf3QljQRicFQTUZRAIIgiKaF1TgQQ8ZwsPccdscBMiMwC80AfGACOctF4n+9/ZJajNkae'
        b'O6wsaUSHaRLzwA7gLuCvAlIUiOSUXUhB1EBAASNKDQZQoUJoCAElYKHB4J31F9JKoSX372py/94Bk920'
        b'tL1c2YFxLQEjZQ9qBEISGlKQTBHVnIaQLD9qUosKQZVAAnNKF9ACDUb5np2MLfthy/6EIDQItBHaGAVK'
        b'g5zld2P0gf0kAtAC1q4cp91q04hCGQ3EKFFMICjEnJsFVUVig/1vzPDss09z6NAMreEWf3v+xSN6lAKX'
        b'4ZxLYqS6LzAU6AI3kb2yjm89IA1K7tm8jWADxBNHr9nA2Z+4EBEhFpFolZ4xcw53ezz0yFZ+s3kz2c+U'
        b'tCiuLDVWA0dXJjegJPMsVNdiqhvw4r63mLz93hyZCZywcjsf+OgFtJoCKsRKu5GS40nYtHE9Z206kVf2'
        b'7EPdmZmfo9t7r9EWjx7v8EsqUEJ28ToD1H44HCMrV60AL2kVLU45YT0IBBFMhShVUKx15qlnnMF3TzmJ'
        b'2e4saMHdd93JA396/IhgSrIH9oACaFbP+8CUAhXfq6TPOSedw3U/uoF2kSgo0SBY5XXJnJilby3aoTRD'
        b'Q2B4qEOMkXZz+IhgDHgZ5XSMelYdAApy5K/550ByGDSdoSg0YyQQQAQzsqZPTqSSlngOjJY86x0NOEKj'
        b'2fqf5noCowWcBkyQPamsAA0DBxfN9aC0hgsKSWCKeaXDxXFxPJVZMdYljnuVwTVQKV9OO+5YmhGORKOD'
        b'wO+AB4E1wGeAdcBhoHiXP6g7a46bwKoCIUvbHBBVBBXJsar6G2qpKYIoKMZZp57ItV/4MA8/8wLP7Zmj'
        b'm5YOAl1yapisTuZY4GiUDsYOIn0xxseX88lzP47ECEilQiGQ71W80tQZEVoVbrnIA3UhDikXfPZkrrxs'
        b'jIce3ss1dzz/fzP9HPAScDzCeQjnkyhXdvjabT+jtXod3dTH3SiT464LNVrW2IDWmrcCUyNUAaTP6LIO'
        b'w3MjNHZPL5VClxwJ2IWzF+EcnO+MCiuKASmWqHr++gBCrkgkb4YumKj2/kVRIAETL06y4sbNvH3Nvcxv'
        b'3U17ic2reuJdYHOofAahKGAwfYjw4++x4p/b8GIAangQLBqujosg7sRMrMydrALfWbZEGdk+ydDO/WDZ'
        b'BKeOjrOv3WAw6DE7P08MBcMNpTtIIIHO2CixUNJggIswMtyk3ylZ8drLNKZeJf38B8h5l/LaRVdA0UG0'
        b'yLsqqCqxhpDLm7p+B3GjjzB88FXaRXbjteuP4YfXfIv+shW4l/TLkuRt5sz45tXfYKIzys0338iyRhNS'
        b'l4GXJIEQhV1b7uGkJx8kyoCVj91NMT/F5BXfzkqxOuIQFcXrJkN2e6Qu7oROUJoHD+AlHB5Zwb4vX87s'
        b'+BgE0KAMtSLLlilTU6/T7SUOvD2L98oqyzYIRZtGbBEpOPC5L/LC+VdRlk16CUb+8ggbtj0IsVFxGIKG'
        b'3P3IbZMqJ1ckckk0UoOda05meqJg7kuXML+8g/apK19EjOAlo0MgAcbGhhkfbyyUVKKCIbhBiA1mzvsU'
        b'z21Yy5pH7qO9axezW7cSP3YpxAILTgBiCNnLgoC6gWvVYnGmyzkOXfEVBi54LAi9Ok1mmwsRUaWwBuuP'
        b'PYb3b1yHqyOpooDktU0r3/HEYP1Gdqy7Hp0xKOcYSj00CtEC6oLcduutLkEZVmV0pIPEgGtux3gqwfq5'
        b'SaARDAoVojoqIEGIURmKrQyyUZAkkCxBFfTq1k1266rWMtBMGjQERAuCFmhfiSoljdigFSOtGLAQ8kJK'
        b'VoxEkhvuhqoQxIlahf0gFCGAKFEVTHEVkAgiqJM7ayqVVIUsjytXcqnKeMOsJNAgtsyyejPo9/t4UYBW'
        b'vTRVzBxxQVzfaWJV/QAxpSyFrlakUs9BD8G8zPOV6r+KTyJVS0yI4ogJXjqDUrH5af4DeJt45/wwKX8A'
        b'AAAASUVORK5CYII='
    ),

    'img/11.gif': base64.b64decode(
        b'iVBORw0KGgoAAAANSUhEUgAAACQAAAAkCAYAAADhAJiYAAAACXBIWXMAABJ0AAASdAHeZh94AAAHdklE'
        b'QVRYhZWYWY9cRxXHf6fqdvd47ME4jlccm4CCAhJWWC3eeEDCSAjxLfgEIPEA4nMgEGIJQQoIJRgJEYIU'
        b'FhslgJQgwnjJQ8Istmc843Hv3bfO4aGq7tI9RMkdtW4vdU/9z//8z1IjZmogvNfL0l0W3r/fyxrv721t'
        b'srm9wc31tyjebeF7AbP4zCK4RXtL4M0oVZlMp2gIFM0l7wbmUGPv81oGA2rGcDik3x/wqD9YZujwTW3h'
        b'nSSWmp8Od0gazxnWWhRUuX3nDtd+8yLd3gp7u3s1oLzuP+u3OBgMWOn2EIzRDNRcWmSsrK7QPbJCUCMY'
        b'YIqzgIjhBAjKZDpJYAxTBVNUFcwqJwDKecnfbvyF+zs7nDhxksl0uszQvJwzm86iZ2o87JcYDnGCmDAc'
        b'TfHsowYm8aU+UlGI4VA0KAaIRRBi2nbb4l01UJaK4FAzTC0CalLdKQq8c3jnEaf0egVBBRHAHC6UFGGG'
        b'OcFUEZtAGfCmFGbMemvMfQfLuSuGGOlzmyEBVCP4hJFiMe6mIS4yxczS4oheRHGUIAbecezBPZ74yfdZ'
        b'u3UHKcfMjqzwzje/x71LH8WQuIs19Vd/l0GoWloiIEJRi84AodvpEoIxmswJCsEiE06VYw/3OfvnV3Cz'
        b'Eb3RI47/8WVW7t0FZ+ChcI7iYJ9glhhRXAWlnc2mhjbASvq5pSHBEOcxU0IANYlPa6DQkide/hXnfvAs'
        b'YgHnosYMjc4pONMKjJrhAMXwebdcwCzBMkM1JDCyDAgkhscUEYleWqCwGT0mrO0OcEShUkab4iUaS88Q'
        b'QkWDibULQnWztE985cIhTUCZUueicdTFMN27y5nf/47VzU2O/vN1pNRaF1W8k4IVgmbTKQ2lLWKLSsKk'
        b'ZqkZyqW0L0PAzPBeEDWO7e1y4bXr0B/hpwdxg8MqoGUuHGIgJkjKMCFrJIMRxByCkPWcHVsqjHsP91Ax'
        b'vAAO9p/+GG9++1t0+8bFnz/L0RuvgCotVJaiZkLpu6Dt71trE2mWiczRkcieazopgPcdRFyMrRil8+yd'
        b'Os/uxTNMn7qEecG8gHNLfUYRZoVPuoBG8GJkKkG3qK1AmbU0FK8Prq0x6PfJgTYBKzrMTNj/8Hm4cpnJ'
        b'PNDb7/OBzS2K6RSxqIx5IYxdyrzKV6vuZvVGUomamAzEeregIcN7V2VGFqA4wbod3vnCF9n87BVMS3xZ'
        b'8tj6Oqd/8TNWb73FyIzbheMRcMQMRGsCrUGNGaqW9Fx/nzOvpSFp/NwyQvTCnKfsrGCqlIWxffkZts6d'
        b'5tp3vssbu/v0Q49vlI4LGM6ikGMfq7PSMpCqiksN2hY0ZAvetEeHZFAc5hx4h7oO8xNnuXnxKf4lHd6W'
        b'gomGKPpGi8hsWENIuSU1K8chIctloVFZs0GsFUozCGYEhCnCLPZsQghx5Mi53hg5GiWpAlURlP4WWofk'
        b'HgcijWypC1izygZTgiqawKkpIZSYBcwEqVp+IwJNx6ufcywPKYxRTFlNgqRWYSGgeQLQCKQsS+bzOfOy'
        b'pAwBhzGbjzEtU5K5VK3bbscilBxMyBKeNiADxuMRQRXnfI4VpopqwDRgppTzGXsPDwhBGY3GvP3fDcqy'
        b'xDnH1uYGly5eYO34cTp0EeeqtiQu1hpLRbQ5B2WhLzE0GA0jIPExPVWZT6eolqgq+/sPeO75X/L6G/9G'
        b'xDObztjd2anmpx/+6Me8cO23fObTn+LrX/sqp0+fwXmPOAfmF2LXzOR4XyqMq6tHGY7HceoAhoMBL77w'
        b'a4bDITu7D1i/dZv7d+9jpsRTQ2NWNmM8GbGxscHm1ibXr1/nEx9/mpMnH2NtbY2rV7/CicdPHXqOynpd'
        b'Ymj1yCqCSyI1Xvv7P/jpc8+jIYBpGtobo+hiS7NYqU1h58Euf/rrdUDw3vP4qdN86ctXIwEtXdn/BzSe'
        b'TJmVc4qiiyDs7OwiaMwcbYweC9S225phlsYYiclh3jGdlXFlnk6yCZHq8xKg4WiEqqYy4uLxhUZ61rNE'
        b'XfgOgVSvzy9HPCdVKGrfRKqQLwEqfDx1ZC/OnT3Dk09+hHI2R/MBoNo0biYiVc9z4upmmXuhODrdDk+c'
        b'/xDOSRzsq3qWJ5RYx5YAHVs9wsMDF+drgc9f+RyXn/kklozEzaUmKrcpiQCdczGrxCWwMSRFUdDpdAEo'
        b'LbcWrWySx492NTcGwwGlBnwKam+lR2+lF0GI4KpwUdGca4gkZNXQnsO1EE4naYZL1bDis93to9HN7W36'
        b'wz7ex0FL4mku1iSkJYMMrK7qjb0r5iQWx1ZfjMtmsykNRElDSZghBG68+irr6+uMp9N4ZrJ0YMxWrGEx'
        b'GUg5tJR8VBDzHAIuMSypd1k+80s8+5kZxc2bb2LiOOgP+MNLLxFCmf65kGtNBlAfVer/YtTyjgKu+1Z1'
        b'MMzUKJgYmjWTQi0N6syg2Lq7jfMeC4GVbsFkZnhxSTMNbxtUUzFSs5ULQE2UVeQshTA/oZYmguSqQLG9'
        b'uU2pJYPBgK2tDUJQXFHE9M2PJvFlZjIb+ZCXi19TQvHrQ+KYQp0vTamP8zzY3eF/jB0MpdigaFcAAAAA'
        b'SUVORK5CYII='
    ),

    'img/12.gif': base64.b64decode(
        b'iVBORw0KGgoAAAANSUhEUgAAACQAAAAkCAYAAADhAJiYAAAACXBIWXMAABJ0AAASdAHeZh94AAAFh0lE'
        b'QVRYhZ2YXY8VRRCGn+qZjQEkLEQBE7iQ4DV3Go0x+ou48N8Ro0ZjuHY1wYA3uLu6WVh2ibDs2TNd5UV3'
        b'9cecc5Q4yZyZM9Pd9VbVWx898vX9+yZhQAgYgoiACOR7EUGae9KrdG9gGGazU42oEVNDTdGoqGp+n65R'
        b'DY2RGBXMGALs7e8y3rp9m3HrHSQMIAEhCRUEw7J0CsBytLflfZongAS/S0ND1jOEgWEYCEMAM6IqwxC4'
        b'eOECu0+fMn72+afc/OAWV7avECTMhFRBjsBBza8tMLD6P1sRADPAMAMzQ+OS87M3nJ4tUAa2r1xm/P7H'
        b'h9y7d4+vvvwCkVAWmx/So8zauyipg6yfbwZiNgOVhqpG/vzrgEmN7WvvJ8sdHj7jj919VDXzJGRgPY+c'
        b'V8V1kgBK6zujGddrI9T5AKbKzs6vfPvdDzw/PsnyAyNmTNPUmN+yEpYVkmoYs3rpZDbzioHqOoaBpjtV'
        b'Q1U5OjrimwcPGMaBaYqYKQAjAtO0TKYFNPv3+fMjTl6+xIr0tLBY71RXoqiQI02baIs5ylQjUY1pObG/'
        b'u8vh4TOu37yBagIjAUYnGOKMSOeL4xMODg5cKmCNwftom7OuQLS8ooe7uoUiZ2en+Zmi2fJDGJLLHKGV'
        b'BSVrmf+bgaQ0kMjdWiSf0sxtXeaENve1pWeZJmquqCAhEIq+vR8wMyRI54p2mDmCzjyy/t4q7hpsVgB6'
        b'4AQRxlU7N6usyJKeyyWJdkZaPSQbdR6AZphCzqhIaABVUVJRN4p6Bl+j/9r/bsMCVADz7E9DfvUMkqyU'
        b'Jtps4dYSvVobrbDhEKlrtvmzwM789OdjBvsvR3VGa8NGZBm3eRmn+qwe5sJcaqBAwMMeOhdV0m2ySq38'
        b'Lb+6s9blklzdNUlGLi3NwFDezPSzLgGuyzSboZZ3VoHW0aulpUS5c2hlqTYP2LoRNZ90/+dj5uWlmKkZ'
        b'NctxobWOrSjcVOlNHLG1iP/zaFdtxQbr33bIWwO0peDtjjUh1T3IFitrZ0CbJFiTmXvQbrX/YRa8O6ls'
        b'MrNCfIOeQ21wm1ujbUUKWs9ebTl+u8O7ijakrVE2NHlpZaKDWKHJhuB6K1BtERb3hPdZRiA3RnXB9Ksr'
        b'KKwWyfJ8XcHw02ZjW1CJPyJS2hMP2mC5bq0afpUrpY2gurQV3kPqL+txhU4tM2U0M0KfzRs3rSaw1DV6'
        b'iZ8rwPrxDdTufWi7zVRGRpxEPWNzF+cPm/CUOiaruQKig7ghTaXE7KT2TaQlCxWXNXnGWg6tsWDpg3LP'
        b'XfvEaptePOC9tuVwF69cSbaqMjqHuulWOVKEzvjbNfvi3iszeiB50X7bDRLSaM19tWpkFIQQAt1ypmiM'
        b'M4s1lXum/5xLq4dHkYNJzX0ARFKTZqbEGBklt45lmwvEGFksFkzL897iHptzhNVQK8+AuqXOgs1gOj9L'
        b'a6iiccJUmZYTYxqpxLgkhNTcP3r0Gzs7O5yfLzCN+ctF2sa0+Wguv7ZGUq8FW1JGMIYwcvrqdcr1GlGd'
        b'UI1M05LRkf396hUxRn7e+YWHPz3k9embXGd6F9TGS4r23n+78CB1C942ZsGbM027ZQFQzaAi0zSljeLZ'
        b'4ozHj59wcnLCkye/E4aBi5cuFje2POkKYuuSxlHiFpHmmfjnmuQ6AYacsXVaojpxvpwYt69d473rNxAJ'
        b'XHr3Mnc/usticY75ByYvo9n31V/uuiaiZlxrP1CZpnvvW02N5XJiipGtrS1MM6k//uQTPrxzh6tXryJI'
        b'4gt1G2TZOkWI/2/aE+kZRYFphlGTXvomlLgSlxOmEQPCEBiGLUxg3N3bgxB4cXxMkMAwBIZhZByH9AGr'
        b'7OuluqBwZk00+c6iyTvtHkxjSikecdOUPkAop+zt7/MPMXYo6zLW9GoAAAAASUVORK5CYII='
    ),

    'img/13.gif': base64.b64decode(
        b'iVBORw0KGgoAAAANSUhEUgAAACQAAAAkCAYAAADhAJiYAAAACXBIWXMAABJ0AAASdAHeZh94AAAIi0lE'
        b'QVRYha2YW4xdVRnHf9+31jlzzpmZdjoz7Qz2AhZobRmBFCTeALkUNdFHLl5IC95IAwQLFKGJIUDUqNEY'
        b'o8EQE5O+CNEE8cVoYuTJy0MhDC230A6VNpTpFHqZmXPZe30+rLX3PjVFCrgyyZxz9t7f+q//d/1vuWf7'
        b'/Xbe+vUMD9awPAPLMYw85IQ8J4SACQgCAvGTEQwsGAI06mCiOK0TgmJiYDnBAoagqggGIgiCOkVEEHWI'
        b'COBxfpBeWMTXm0Kz5RkbH6PmHIZhZkj6H5dRfDQBEUHVoSKoGSfaC7SzNjVtMFCv45yWwAEsAJI+GwSL'
        b'ti3dBYahLHZqeJWAc4qqYhBNiGBGYQ5L7PRfC8EQNWZnj/Ltu+7GgnHd5qu4eesW8hCAkDBIspq2NktE'
        b'K8USE5xzeBQvAiqWqJPyJpMIJf6FEppZAm5gGRyeO8Ls7CyC58DBQ3SDoRbQCgIiFdPxJ0GKMEBADE0u'
        b'9IqV1MaHE6jCR5JAWQQlBTgDQ1mY7yBiKEZvfpFeL2NAo1tFrNxUErtU0CqGkLivCUrI0mZSPSAgqqgm'
        b'us0wE0Q0PgyoONTVWTbUwMQBEIIgIYssFDFDBIckVooYLK9a5RcBbyFHrN9ZxUVBgrJnz4u0e23Gl0+w'
        b'cvIsZva9xsv794GB9zVm3zyCZD1yEebmDvOXPz9NfaDOUKvO6MQKzlmzmlajSV2F48eOYZazdOkIIR00'
        b'hVc6g+BJ2VSyVGaGMf38Xnbu/C4qxtq1a7n3/u3s2vUb/v6PZxIDgpClWBP2vbafR3/xszKI687xyCMP'
        b'c+7GDRzvddlx9w6mzl3DXTvuITqziMe4Z24BbyGiDEX0p5iyPEDIUefIO12WjY7QPtll/8zBCKIoAwXX'
        b'ZVSEMkqy3Gi3u5gIR95+i4X5jBWTo1iqT0XGFnEbDNyVn/74g+MrzqLZGuwLskhAa6DB3IKxZuUYn9t8'
        b'BX/929PsfubZdKJTw/J0y4DZ2cN02j3m5k4yPjnGNVdfzdIlI1WGJTPqlE67i6fkhZRZlug0mvUGt23d'
        b'QsMbTzz+OH986k8QAmCoczj1hDwnD9lpAQE8v3cvz+99kUazzjduuYWzJlcRyrMYJqmAWtzXYxFpMFAp'
        b'SI9u+/eB19jx4EN0Ftt0em1Qz61bvsbWb25h+fgklgf+8NRTfGfH9ncEVFhsL3b41WO/JkiNL35hc1+x'
        b'KSI6fleClWko6YYY/MLxzgInjh9nsb1ICDneemy+9mouWHceK8aHmZwcYeqiDeBqFIn8zsvo9npMPzdN'
        b'KmmIaGw/qogopinMVT0qiiazIoIhdEM6haYsAE52ulCrRfdLwOupfevd1ttHj5KFPD6jgjqHqkNUwQI+'
        b'5IYWRdBCanyK4VFi5EtIrSRAyDOoN3BZl2DQcDUKt3MGoMRBpopXh0tNOhGImeHzPEe9w6ny5sHDHDj4'
        b'OnkAcXX2HzgElsVelnrak7/7LXNHTzA2NkpzcJjp56YhdMtkfze3WafNC9Mv0ev26HY7DI+2mNp4MY0B'
        b'j/ceuXfbNvvENVfhXY0Hd97PnpdfJQa5kec5wfL+8wEK4ktGlJxglhx6Zku0hnhFRWl5z09/8XNWrl7F'
        b'wmIXbyrkWQam5KGHeMizOKSd7oQQwLqp70kCc2bxE9FIBB9yEKiJo93LYqiEgA8i5CEwONji+ptu5pVX'
        b'XmDmwOvMzy9wZO4oMzMzpwFFNQ28x9Vqtrh883UsaTawrEPLe5aPL8Ol7PchxB6mNWXTpR/jok0XEQBF'
        b'2Tv9Evft3FFUzfcF4NQlrBgd49YtX2e4VcOJgRhBqqrtzXJUHSGkUUAETfPy/PwxQJHYm/8vgNQpdS9p'
        b'5qZvJIEQAipiqLpqEhAXC5bC8JIm6LsVvPcAR5TxiXFqLvQV4dTPEgB1abIrBiURRZ1HnWdy5YcYWT5U'
        b'9ZQPtBTVwKZLLybV0qREKoYQqnovaUoUkVTOheXLJ/nBQz/kzju2s2rl6g8GR5V1687nums/jxOfpsh4'
        b'zaquhkoaSou+IoV2EgXLGZ8Y55OXX8Htd9yJ87X3CUdwCtvuvI3BoaVRjyVqiom7mJ5VUqct516NKkAE'
        b'NARU4UTWxg+2WLZiZbnBmQIREeoDjpu2fIlDh97gZLeNc4WsSswUDZ+oPsqJTejzp8GLr+7jxhu+ym1f'
        b'uZknf/8E39p2O0PDw/TPif8LnGBceNkl7Pz+96jXB/nlo7vY9dijBCuerNRwYcf/tzQRK+gzJiYm2Xrj'
        b'9Uhd2Di1nnNWb+CB+x5gz/QzHD7yFp0ezJ88zu7d/0TwDLZafPgj6xluNphYMc6G9edy2Wc+S915Lp26'
        b'kCs/dQXSaWMhL+RnnxoRxMADWEFJOS1GwOOjI9z05RsIBiEPmBiXbJpi08UbyQ1yqfPqzBvsfvZfeIQL'
        b'11/AvQ8/TEPASeyDZhkSMlRgYnwZohp3MUrZ1R/HXizE4ai8UJIZi6VJnKFFsGBliTQBp1L2NRHHfO8E'
        b'kGNisTcRhaVY4QUtFYaJlPtFUakgikes9GCRioU0KcxUo6altw2xNDkvjI2ORF2nMDTYxDuqYyXmLYVv'
        b'KYrL+Kjix0QQVTwWtX3UI6XDyuJJSkkrLaTpMPl8aOkgg40aA96z4aMXUK8pZKHaPYoqpJQOBY70i1QH'
        b'FjT2sppTnFoVYMUppBBxlSsLOiOjxpJmgx/9+Cd4L0ysOhtFQSvxV7AgfawXmqy0mTpBQPCBgDrFF+1B'
        b'qeZjK07Yn5oFIkOT+Q3nn4+pxMEt1Y1KkfbpdCveM1XTVpXwkOU5fmrtGpqNOnV36nuQ4nWJpAC2PilO'
        b'kgPlmxIfNwhWAHFpy/7hLRoI/WctXFW8c8oMf/Y56xjw0X8hiTODNKNU7gsU5QHMhGCCBCG3EDu2gGjM'
        b'RCz01csyaiqxXU4WQghCludkvcCxt07yH3ub6OPe5+5LAAAAAElFTkSuQmCC'
    ),

    'img/14.gif': base64.b64decode(
        b'iVBORw0KGgoAAAANSUhEUgAAACQAAAAkCAYAAADhAJiYAAAACXBIWXMAABJ0AAASdAHeZh94AAAIRElE'
        b'QVRYhWWY3Y9dZRXGf2vtfeajQzvQ6QeURmkpwaBQoIQiBIQLYki88cJ4JTGo/5QJdyZyZ/RCMUEUURQl'
        b'8iGx0CkFpdMyM53vzsw5Z+93LS/ej73PdJKTs8/ss9/3eZ/1rGetdeRfH13ySsHdwRy8JbSBEALuhiC4'
        b'G/HP8fzuDgIg8Tp+KPflwBMixLXSdwRBJH9LoJpi3Aypa42PKIar4yEv6wieFvSyFUTweVHcexsnYO4R'
        b'gXvGnG6lp5yJ9RBHaBCcWhXcBXHBMMwdN09bOJEcA0nwCjbH8ILVcUQyW5FBydQkfLhEbB2hiR9BUWqt'
        b'qFHFQ3rYYnjcDbe4uZdTp70TIzgRuGTWevcKKTlcUtbKZOU1BUFFqEQwGaCDappKNZ3eseCRpfTK4XCs'
        b'++zeBTNLL73wDkyG54XWngB8UlsigodAPTU1jYWGJgRC22IWupVTiAQnyxrvJCIIVgQvSU63xSNKuSO2'
        b'sNZ912NUMOq6rgGwEMEUphILgnRgkCTApAWJIciRyxtHbVlaz/BgTM/OJLV0mZjDaAKShKWVVvGfZphZ'
        b'yaBEZJcLApIAaL6WIqb4vDutB9q2Ydw2jJoxezv7vPvOO5iFCWPoJ1kXSkdFAbeeWL1skkMgEoUnOCoe'
        b'ASGIe0xhd9xaQhgTrO18Syve/MMfmZ6dS0tbumcRQpey5U81+UUnN4pIhLihFMVGi9jfH7G+usL66gpt'
        b'sw9VILgTzDHzJHJn8dPPWLx8iYcfO49oFcMao95ZZAIlYghG3fPKnih7rLljHmjGDZ9cusp7773Pyuoy'
        b'47Zh2ASkrrjv9ALPPfc0d58+i0iFunP92jK/eu2XPP2dZ5g9NIu69b2xeFH2NvcogToLLaL3BNpxi6Js'
        b'2padnX3e/tO74MLFZ59mfn6ene0drl9b4sPLV/h8aZkrr77G+Ue/xYsvfZebX23xi1d/zu6tHc5fuFAO'
        b'mc0xg5GycZaSUIuk8KQXCamZ0bZj1tfW+csb/+CRJx/n/m8+gBiEEDh+4ij3nDrGnXcd5oP3/80X//uC'
        b'v/75b3x26SpLy9e4tbXJUxef4eSJ46lUxDh4SrNMg5RSEoHVktxTVMA6/3A3hsNd3nr7nzz6xHkeeuwh'
        b'3Cva0CAeUFFmZmc5c+4su3sjVldvsj21xaefL9I2QwTl5Km7S556jpfToyQDkQwXjYKi4zDmNObG4uWr'
        b'DHf3efjik9TVAHJaak0wp64rpgYDTt97D9P1DIIyNTONVxWOMDd3KOkkMUNvHw5iEtwFnfhObieANgQ+'
        b'+vBj7jt3BtGUPclLpqo6AVQqrTCDufk52mCoCIN6CjQy4hNZ3YXMe2Ek5ZIT+SATFnUUI7u/u89/r13n'
        b'0Ox0SYkosUBrY3CnbYyN7W22b+2gIrRmgDKoB2hVxeLrfeXGrqIfpsk2BOquYcnvEeqt7R32RyNW19ZZ'
        b'u7lKrQPcAzPTA3AhBOfGVyts7WwxGjfc2r2FGYCCCKo1UQ7aKxcH5OPgGVjyp7rX+KX6FK+b4CDO4uXP'
        b'+MZDDzDQGfZGQ+46dpSBDFhevcnW9jbizt7eiBs3llEFR6moMDWmpmYKG9KrBBLLQwSeXT+ZU521U7q4'
        b'5BFa1VQqXLu2xPKXXzJ/9DjDvRFbm9ugQnAIbWC0P+bKlc/Z3N5iMKjwRmijjFk4tpC8p3RVnQPfrmt8'
        b'whjTtwVDBA7PH8ZCwDDeePPvvPDCUyADWgsElOG4YTRsubF0g8VPP0FUCWbkrmKqrrn39KmivVh+eqHK'
        b'e5ZWJh6izukl6cEYf+XI/DxHDh9haeUmmzub/O71tzh172mqmSlA2NvdZ2tjg42bKzTWgsQsjC0HnL7n'
        b'bo4dO4oiB9pbwfU2KSUMTi2iMbsKpfH60Ow0jzz6OEuv/57heMSoDWx+cinFnLh5qne5BnpqXyqB555/'
        b'lrqqCgvuHq2gRKsn5h467QtfRcoHBZ5/4XlOHl/A3QhtQ7CWpm0YtyPMQ8wiAFIfDijCuTNf49sXL6Ap'
        b'w+KBBXHtBNz/fwYhgmYNaW8cEBFUhYX5w/zo5R8zPzuDihd9RVaVbKL5qCLC4TsO8cMffJ9Dc3d0nld6'
        b'3tyLT4o696BVyrpyCs2U5Q1UefD+r/PTn7zCnUfmqaoKEcVRgkEwsOQTtcDC/BF+9srLnD17P0hFVy8k'
        b'tR55OJzsMOIhkzFvrG/61toKw71dWguYGcHzZGBRL8H4cmmZX//mt3zw8X9oLSDiKI5bYDCY5okL5/ne'
        b'Sy9yYuEYnkIRZzmJI1VpADubVFVUhUqFqq5pW0PW1zZ8e2OV4e5ubDlCwDLNZVpIY5EJK2trLF69ytbG'
        b'FqLKyZPHefDcGeZmpghe9Rw59RG5R+81f7EZE0QlAVKquia0Rm1phs/RVAHM43jT6xZEBBROLCxw4ugC'
        b'eSbJAXEsB+Y2AOU6N2YJMCmMne1U1CE0WB7aJmTWUey9Ei2S8tSlG5fJE6kcWONgC++FvXhf6WptVG/d'
        b'NmMsDVbWGxBjXfPksF02xaXSJNIrxvG0HMieyavObzwesnMZ0jbUbTvGLRQLd3MUMHEwn2jwcgHMrqvS'
        b'AXWPXWc33tD7uaV7vh9qBIxO5oJQW2gjIwpi0tHZLzb5odJB5fU63iQOaOmkMvH7UfdAv3/uGMphd4Ta'
        b'2zG4IR4QDI3yQFKYvEdRGZMSvZ2XdtlTDi8lpzoGxCdC3zl9zOKmaakN0EpRMUw0epCnopMHyBSF/q8f'
        b'aZ3ovmWUkGQZUm7nVxlIpSf+Ujok2YpTb23uYiqoBTw4bfqBAO8KaO6nD/bHcQ8v7zm4kSktGVk2V+2M'
        b'QqL/uFRYgDYow+0h/we6ZEnSBEXTgwAAAABJRU5ErkJggg=='
    ),

    'img/2.gif': base64.b64decode(
        b'iVBORw0KGgoAAAANSUhEUgAAACQAAAAkCAYAAADhAJiYAAAACXBIWXMAABJ0AAASdAHeZh94AAAIPElE'
        b'QVRYhW2Yz68lVRHHP1Xn9L2P92PeDAPM+APESCCCBNGIQnRDCCQuXBliTEg0xoUxunQDLPwXXBm3JsYE'
        b'TFxo1MQNSqJBUSNBhUEiAsMwM8yM7+d99/apclHndPcD7ku/e2/f7jp1qr71rW+1PPHk9z0lBTMSjoqg'
        b'oogIigDg7RABERCoP0H9ivhwtQ93UT9JfI0LkWon3hWXGUdF6FcLckoJxFFpNhxREPHBiDcjCOjUi1je'
        b'q2cujo9+jC55O99sxs1hUynWg2ToIceaSt8L62tKUiFnRVNGVUajIriHkXBwNDysMfo5+eD1vNR3RVVp'
        b'YRbA3bDe6Zc92YhonNre5u6776IAZo57wbG6f8e9pUSGP6pTQ3DrMo4jLdHu+LH01l9cGS2CirK3OCSr'
        b'xJK9GKiiIog67gJuuNuAotHuu8PRslGvaeGq0Wm4Gn5zMARHwcPplARxISd1DCHlBIAquI3IGIBcFxOX'
        b'lql6xhtMkGHV49FAvcbUx/8+AXu7XiGrxkkRCzBXUJs51q7UgoshxXBxcAUjUuqGWHXPHcRwEVwFSw4J'
        b'Mh1KprhEFKepGyEKQB7w547WUnP3WBjl5avn+PVLv+I/e/9mj2ssWYRR19gSgrvgYriUqDQpERVRkibW'
        b'bIub1z/MQx98hM+dvY+UHVEF89GTiscs1euhGjzKF4MXL73EE395nINyFRJxtALR4/h5z2ev6SyAX+G1'
        b'nf/yzyuvcON1J7j91B2gNiRwKA4VstdKEGR8B8wP+cXlpzk4ebUafR8npqAWxusAJjyGR/L35Rq/v/gH'
        b'brv+Ywh5CnVEIjO5WXezALMGV4j0XJYLsAb071rQoQIsPpc4Bi4SEIMyBbiAzRZcXFwCA1OPKNYqbLDJ'
        b'rZoQjxK3hKiAdFxfNsfISDiRLHHT/EZO2SYbktmwTTaWXVSzCyY9uHOlu8LfFq/Si2O5OoVT+j28lCh5'
        b'aaxG4BbIkSmv9FDL3WHucz6+/nn+evEcxoqTG3Nu376Z+08/xCftAU74Gp04QordKXhyJCUkdVwu5/nG'
        b's99iR3eCoyQw7HqEIpjLyGy1x40OtbQ5mNSIaceXb/0SD37ofsx6tn2TeVnDzTE1RPvaHMvIfxL7TShb'
        b'i21UNjDZGWC1MlhPmVQz3lgd99o7ndyaXgOzA2KOCXgytvUUUlZo0eCd5KgHR/XZhvtQ6KxDZcbM1rlm'
        b'V1h24K0yAe/hzNqNSNKxxdTW0xg7Ny/EI5869Bpq+/AIrziaAs1WKVmkI5FZdAvOy9u8fv5NDq4dsjzY'
        b'41l/jv3NC2MxFJgX4baTH8HbKgG8SvEBl+ytcQqhf7zms/YwpzK2OqaQXCEVUjKOVjs8d+l5fn7hl7yw'
        b'+xILc5w5dD2sHUEXfIbBibTFY3d9mc+c/QLYtOk0pyKKGZs0E/cIr7e6rjWuFeyScBd+89aP+d2lP3Nu'
        b'703+J/txeQFIoIdR8zZSw72ze3j8zu9ysjuDWlMQoyMOaJVagaF2NH0jNS5eb5YCriTreGv5D374xtPs'
        b'+3JUjg2hUsnIKskewRdveoTvnP0mWRNuffVRAa2VXQvfa5U1DhgUg7QIxaECabbLzsEBb+3u8tQbP2G/'
        b'LI+TY2slRaFkSIktTzx8+j6+dvpREo75pP9p7X9UHvJR0uSp5Jw65BTcYbfb5Ucv/oDn33iB/bJgqYXG'
        b'7wMQah2notya7+Arm5/l3lvuY31jC0lKkYiAatUYaG11TX3WamtVJqMndSUHN8ydn732U3772h+jfaT6'
        b'c4tMc6qm7Ew6xfc++m3Obp5AZ0KpvKS1dXh1JvpTk7QVJh79LA9YH9vKkIPe93jm9WcY0t7A2zCDQlE6'
        b'7bj99K189cyjnOmup0+FLEGQIlqpUhF0oibHDQlStbqShwbXJoHqsyKc2/0XF4+ucuzVGnQR1pcdD5+5'
        b'k4duuJuz2x8g6Sm6WWHWJZIoyRWRhCbBUkHSEi/zEGriiI/OSe3AWYaRpIFZEFE6nL+/8yLW16go48YE'
        b'IGE2582DQ546/zKzt1/Buzmz1KF5BbmQyYiss8qZMivMlsYD2w/yqRvuGVrU0B8k+DG3qUFEK2MSw2KC'
        b'V4/OR3pq6icWIBUWWwf8yV6BoxTnlyU4SOy9WilDPkosDrb59PadWKcxC04Cb0JESGp5D+hxpQi8wz50'
        b'E6MN90I4n/qKr/74NRMn6MYN9YvC2sYlDuUA8XWENEIWx82ryLeQj6EYq7CUHlsuwliTr1PVKONCw7np'
        b'cMbkfPvq0M0LnjUGAvcYCCZxyk3NqYRgMTEQYdZvcYt+gsOtPfr5CtEec8dWDqU2WQ0NLqbHyxeBFM05'
        b'FUhJ8E64bke5Ze8sqcyBqt1rxKViN8fYFQNiEGLkXzrhyXu/zqp7jJUYs6WEJq0OUNWAmCBuqDeNESP3'
        b'SgVPEaReV5hmuHnO3FaYC73WdSZAEySIUTVGWdyH1BWLAOalkl3qgjWcqek7GYfDmMmbrKFDKhs7iVmA'
        b'Vh1PKaSMpGPzgFTOygFoIdWZTPBhXlIEr460KVPr9GuDYhDatC2imIO5j5xfxZVJ7eztSYhK1fFRXVFc'
        b'GkztoiQFxVCXUcXV+1oTrFsJVvWR1KU2SiOeD8hEUzV6a9Nflc9MXMaR2IQIGTPQRFYhicViA/KlIa7J'
        b'tAaT2iSrJmirNKd8nBO9de+mIHzq1FB/EcXi5NKv6LoZXcqhWURHbniftjKMUsdeA98Ot7WYTMVEEzVw'
        b'fBNSo+nFyO+cv8h1Jza4kAQjHlSh9VlFVZOiEjs99uSrchfxNGQQntqqdRzRtT1B0bjXBtkhGIlSYLUS'
        b'Ll+4wv8BmIZFYqwQE5YAAAAASUVORK5CYII='
    ),

    'img/3.gif': base64.b64decode(
        b'iVBORw0KGgoAAAANSUhEUgAAACQAAAAkCAYAAADhAJiYAAAACXBIWXMAABJ0AAASdAHeZh94AAAHM0lE'
        b'QVRYhW2Yv48kVxHHP1WvZ3bvzt7zIWF5z2AkCIwzB3ABIBxgRAISAf8CEUKIjMhEBCQkSAgyRGgCIkSK'
        b'yBEiQIfwHUYn+3znu/PZ6/XO7nS/+hK8H90z617N9nT361f1vvWtb9Ube+ONn4vlYWBYvzCzel7cN/oI'
        b'oI5ZHAIBSAhQu9HmMAhBSJQ/I0uQJwbqC1L5dEeKJdyKU1K5O4+olnccqla7/epQu146RHVIIDMkI3li'
        b'aI54cg4PD4sBt+5UmcCAwPCySrNiZQ8lqUNT3an3EZhh5riXeYXI1aGI8sp6MAaZESE+c3TEV27dIkfG'
        b'zYtRUw+TAeZefKuhtPrulKcKUHNeHRUwzL08kohpBERIRM5EREEqxPnp6RyyiOBiuyXn3ICfjVeP3FNd'
        b'HZjNzi3B6l9tEd7IBSHEeHHO6uAAYagu1s2wIbFarRk6Ud1ruBwzB3OkgBBRSRGhBVVyZ1sZvyC6GYry'
        b'jjkooiDqsFqvCmL1Hu6dGubGMGdRgdYiIA1EGhiUISaiQlC4BaZd9NpnzqRKDKlyTbjA5GSMUGANVpu5'
        b'amYMZgWyxhMAKUMkvvir33Dt9r8Yx3OUM0NylKxnnyphG3GtyoObMUwjlqNk2WBsjp7hg+9/j9NbX+Ui'
        b'XS3QWeVdZxsMhmMEzmwkJJKCGw/u8cy9t4goK/KqGgh8R4jmk7oUzA/kcLRKXP/dA+5dnPL4te8w2WqH'
        b'd11mKiSLNFYxHoJJeAQDQSJwiSRIAu8flU+lqVOcNZWsKvfEkCcOP3zM8Z//QiIjVfQWkQFKlrU0sk5M'
        b'w8MYLkZMaUGST5lh51iYsJIQfbzAcsDF2K8brur5RiW1zbpiVkDLytz9wXdZP/w62zCYtlgEnjOWA1eU'
        b'ReSMRy7fI5NiBDPWT0+5+Y+/4WdnO5EtPjqKknXzUtQQqt45C6cK1z78xtdI5hX0OqkZSdbDZjXTVHUn'
        b'JJQDf3LCZ3/xXw7u/mcHuDysCZX5rP9bhqw6YAYRgRRd9JQGJvMCq9SdynUer/zzmgiqCKSAVeQyMIBU'
        b'FowbduUqM+N2mQAwuIHcSG5EBDmCIVlNy3JWLZhQJN7yhGcKbhUlryiZwHNmHRmPmPlnRXTz9Rslf2pp'
        b'aoRqwwa6lzN0s+ctkeuIEJYzz75/nzj7hIio9cuRe6lPIXwMDt99RHr6QYdAwOQrHr36KqG5velf65hB'
        b'tST03qRWf2vSK8MJApCCg9MzXv7lr0nv/A9NIyg6cjhgpRSs84SPmwVCxtkrX2bz+rcIS71X2klYMwYp'
        b'6sqq/blMtzUATbBgyMHq5CnrzccwjTPsag61ir+0Jghjc3yTrQ9zklvFX3TJGVjK/0Ice/a1NkswIFYK'
        b'3BJEruhQVZDOs0tHGPKyaNeyzncJnEPWrue2Ym9x7ZlUKn/AxeEVxtURscp4HjFljAoQwlNV6TyVtKs5'
        b'cfj221w9P2Nz8GwP0T6Qgy0WCIWUyekta0e3ZuP5c9e4/bOf4NmIYYWdn8PFtjR1IWycSCQO3n3MF/74'
        b'W9YP7kN19uqdt7jyh99jP/xRyeKK5jKdhtb/thbzkjq0pri2oZGczfFNwJEMQhhVt4AIw0IMxy9y/Nfn'
        b'WT94r4d/lSduPHiP+xZIvhOuRvKhqyuGu2Mr7wJX+ppSbBWlp5ZEsCSug4r+hDkZxyPw7AwXjWPzyTab'
        b'Mp9Ue/MFRoKhBxjrPXFZqbBpxKcJiE4wU8PQWhx7aTD3glwEnke03bJkr3nrAObGbv8Y2mizglSVHkLw'
        b'/O1/k+7eYcwZ206sIhfRV+OWQa7doRmKTA5hk3H96Qnrh+/MBO1c3G13L5WOIhsVmSqOIcfTis+/+See'
        b'++ffidwcKeycyS4W/Wy9rqcQlmurkSpCZuTDq6VhCmsblB3HhlI4aTW777mSOz5OkCcSuULdbC7Es6eo'
        b'5tC3Y1HH8FLrNi+9WAjdEsh2hXgoE5UdgLeGn1IgPXIRMWtaoppN2jXanNknRYegPDi/co3H336dbKlY'
        b'0f48TRit74J6+uYpOHnhBbYffYm8Tti4BU0VlNLaWs0QazuLhUdKCUtGrA4Ybxxx/rljnrz2TT5+6WVk'
        b'3jusZXFQ49B+k2RmRBJ3fvpjvFbytm1xShPni5i0180W3AJQkBHZykY8uuNiGXV156KEzN0qQmULXLYy'
        b'ZXCYekNuGLktq+vHjMpuIahGWsK0J3v1sl/Xr0NrWVOLqc2e7/OzQaEqDTuitv+TTDvaGFWu0n5lUcVG'
        b'vcNQBANVNWPn55i57dDCkaaP3dZ+Vi1FdpnPoR1HWtsHS8dKCz3kPKGcUYwoT53hc1O5DMDeoj8dk12H'
        b'FpdWFxbzanpDKCjtc85l02YKIk9lf09VQLjUIjQuSKoSMnNgx4Gl503VL7U2y1UZ4zgybM4+YZq2nJx8'
        b'xJPHj0gpkYYB9y6vl+SdhSOqu975mS4h1/jXalibpJWqQAjn4ftP+D/Yz2T7a8fRGgAAAABJRU5ErkJg'
        b'gg=='
    ),

    'img/4.gif': base64.b64decode(
        b'iVBORw0KGgoAAAANSUhEUgAAACQAAAAkCAYAAADhAJiYAAAACXBIWXMAABJ0AAASdAHeZh94AAAHM0lE'
        b'QVRYhW2YzatkVxXFf3vfU/Xe647d2pgQhLYz0RCkcSAICoKI4Mh5cKYOnAgijiSgIv4jwYEzJ+rMiBDI'
        b'H+CkkRCVpOmPdNvp7qRfv1d1z14O9jnn3nrxQfHqVp2PfdZee+11yt74ze+EQBGYAYABIh/6Z/nYH5Z3'
        b'NkayjBfoYGR/0nokmGFm4BNBYXf2nDIRCJhVVyu2uWZEW8NkCI1F+8ZmwsamdrDneKvIf1p/szqpV8QM'
        b'YZS+RWHiypUTzGxsYJ4TDBvzzUCWI8wNxzEDz8E9XJCQ0eau0TYMLcCZ4V5wwemzM4pPzlwrn716hZs3'
        b'X0USRAbjfWMzzDSC0kEKrb1NdAKQDEltP8vxElI+c4CUMBzMePz0lGLuuISXXNQQOLi37QzMhfdToZa6'
        b'FoytoMMytcoxGpnJ92poG+SYyDX72dydMj5ZfZGIMNAZiVC0NGRYZmpjHUNIIhgDwFbUdhu8aZRaiNiz'
        b'4EYZ3JAWorbKaZlv6xq+2bAtRhXs5cgLk81YzFglYfWC+8QsMbc0ITExU8MaamoFYS2NAxPKQoo84Shj'
        b'deLVwau/vTPz5p93zPMWhREhpmnme9+a+dH3Cxvf8JM37vH+fcephFrJOExHlR/+4Brf+cZLuGUul5oF'
        b'b0EVM29pWSmLUpMUjQtRiaj85wPjX7entkqF6qAtGyZCZ9QQ9+8f8+DhLnfQqDm0NT56WhoDO9EZ33eS'
        b'e0/lkJ9WiiN6BRFiVwH2sIsMJAxiYoojvnR9z6RTvMzsZ8O0ARVMBZODDKsTRmCectARslWlupEBdVKp'
        b'86wN8k5CC8wCY4/VKVmpCrHjM0c7XnvlGcY5zMHuPJB7bmi0lxCVrZ3hB7noLF0+K60qmyAuf9Zgm88m'
        b'/vDHuzx5bNx6dwv1CGzfiGl8/SuPefnKB4gjdF6IvYG2S6oQpgxIdb/wddlplQ26Ugu3dTh9oPjHrXPe'
        b'/NMeYovNBfkOCJBwE9/95gOcGemEcwKZMCvLGAkRQGXez0RUMjHTaqflryARoRWx140wePT0ObY/Ak2I'
        b'mjxq3x2XU7725TM8YG+RiquK9QaoAKLpV7CfQWGL8ndyj2YligQRcQDjKHvgn//eYWxzbVdyRwFmXLsW'
        b'vHh1RtMEPgEb5rrDIkiJ7OgEXsV+JwIxrc7eWDpUvETXn942xl/w7GPn7Xe2qUNWMdVEqQXkT8Vbbx1x'
        b'8jJcPqnsarCPgimGShuOTIDz8EOjambjpbWSJWk9N6VHaSyqqXa+v779hEePPgG2yGuqOdk8MfH++RE/'
        b'//0WtIPqWJyDbXAntaz3PINw4y9/P6VcfcBPf3wDqxp2pGsTKKusI6QVOsK49e6OoHGQVsOtO6sGWHvF'
        b'BtMEKiAHhKs3yKxGw5BNvPfejjobZYTQktXkZullqyrLxmk8eLhvXFJ3CgmusmrwGGezqkzVSn41GJKc'
        b'NBOXj0t6p9FhLyDkvbP7aKWAMyE+2j2BzTGEQElUqUJUYM5FvabwTRt8t4XI2ciamZuQ1XagiRtffJ5z'
        b'ovmmFRiGNfsBaSEGWhMy+PXPvsD+dKJExbyiSYtjTAeXAiCxV3CpTvzyt3d5+AiwTcMqMIywiZuvXuH1'
        b'1z+XzdW8tZDFWwko3m1lM9ze0oUZN65/PpHpzdS7r+5FsGiWFFgIO6oZjFki151mES++sufS0QnIh1df'
        b'mSeQKMmJ9MS9fSx0EjLLxs2UHluLM8G6M2wmrbTM2AZ5aULayTdzcmliIoNZC8zS1aCACKmlzDHF+HKY'
        b'dJpGNbN1UB1anhxnnudsqFimdmV6TrZT0kGHV6eeOEk4K/1Zjt4rY+1J+ocr8o+Tdk+VzVXKVMlBbmAT'
        b'pg2Xj6YxX6vXCErKsu+9rAOnEdiCrV2EuZ9y7Z1CpIhaypGl/zQ5FsYLx9OyRl/Xlhykfilbh1sj7Lq3'
        b'asnuWubpgYz7Vr99ZK8S88H5RQroZuvUqiZBHXUNz5RY00z9p+zHsvehhaKdpyO6Dgqmkxn8HDRnI2ZG'
        b'5YwoH/PCZS22uAczVs9DlZ6ai/H0Vtun9KbxKde0Cton46uvPef2vQ1RC9FKH9tzvD3n+kvpoQY/bcXN'
        b'1hGKSQsftASXldDNtg04exJ6/xlKa45wfvWLb2fVxpwdXUp5aBYlFMm1rn9rzM3bNchSqbtGrW+cA1PW'
        b'C3Tyr3rgyprKLH210a5CDe1axx3sYNkxXZSFrjFgWxR9KfvFsax8pXW1tpzfJCQH+dAbdeRHapZglqpL'
        b'gW0BNe/S4D2AashBXDjTiHps0q9QWTYrDDotbEFivdT6nlyQxo9VedUB7CJ926nGXX2V+07SFXL5WVPw'
        b'fkX/P4WzMKP9LhBQvE06cqOYFjKzQsouVtfiBA8EwSw1h+XnGGwR2hHAhQaQgTvzvlI+vHeHT549586d'
        b'u5zVwN0PqstatzUM755p+Bf41LFpRB6tr4nHmpPdvrBwsIZx+85/+R83/VMFktBp5AAAAABJRU5ErkJg'
        b'gg=='
    ),

    'img/5.gif': base64.b64decode(
        b'iVBORw0KGgoAAAANSUhEUgAAACQAAAAkCAYAAADhAJiYAAAACXBIWXMAABJ0AAASdAHeZh94AAAHYElE'
        b'QVRYhWWYS48kRxWFv3MjsrpnBg9+YCwbCZAZwQIN4AU7/gP/A5AlBEI8d7CHP8IPYM0KhBcgXgKJh3gZ'
        b'I4Ntpme6OuMeFhGRmT2UVFWZpcgbJ26ce+6J0ne+/S1HFHCjyqBAEkKEBID7V/9doHENAhkj+pB+LwTj'
        b'WTAymPG29jkCTECcuM6K80yNCKxEmaxORENRwEYaQSSCjkTbRMfXAfiYfIKxj3cC9wX0USIUpB9hnfAN'
        b'1DYG5Fq5c3eh1qCUQi3RF2mDhBRIAYqRCW1J6KvVPo06SE9ooj8fgVRQBBGBGDHS0BKvK9UIC1548QN8'
        b'+rXPsKbJTExDI9H7KrUBmpnb83O4OGQFTN76SYeBPWORJgSPrq6oIw3cuLHaNImMAIOc2I20OwRpQAms'
        b'GHH7gjTxDp4cNzY2aH2Q3KN0WgiRSCId1FIg6dtk1NMpCIPSyEEm5LbAOLzV+SAdiL7R43a21LMtC1s9'
        b'6wKcRPScR4EqjWqyKRFk9AkuIqgZtAZNsLphMTJTDoA6aRRlrzz6qp0NZ0KuyElRRb4mtZB255gGGAlJ'
        b'1JBIJuKeHSJIr/zq+z/g7Z//BmnlpAohLJG1wlhVGiKNndgJ4z5akm6ETU1z12ZJUx5+khe/+pUuH85R'
        b'adqyXvGsFm9kFXB9vqH84U9c/P6XXAMNKOMd4z7HdTnsUBxoO2OF4AZ4jHjmpZe5WhuXEQQeutYzFRF9'
        b'y3wIMEu6JdyoV0gbkyVQx7h86n2omw3U/G6AC5Rm7l+Y8BPwRS8GD8KOaq6ThSGQBzSr60XecD7yk53c'
        b'Pny3pzJ0zFTpFMMNiqHdv8tlDUiGTnlvBRsgdxpOgk6SOnNb9dyi88WJ5XOfpz73HIuvKJFbpQVBCVGc'
        b'RCZqSeTK0hqn9Zq1mfjsazjuEqzYHFS7v7YMdaTe+02IlibHAw24EZzv3+dDr3+de88/S+hM1TXVE7iR'
        b'jdKQpmRDbSUyQSZkKEb0SpU3MdmYdxsQ6qijb6sNY/2dQ0WglZPfQ7qHWLF7D7Q9eGOCHKKahLvqh7qy'
        b'i7LviGJLQqcMVG/d8MACj51zbPgLsKxQCfLOyrI0tF6PjZzVAuHsgKKDiugZ0tCtY0Zuq3+HUPvtrv0a'
        b'LT4SYlB0VuGCqe9d8cwbb3DnwQNWrkkComAFUQpFQZGQ3WOkIURcVrJWjAjXAyxvLsKGytCgYy+aH+v4'
        b'PQ+g8vETfvuNr3FGpHpmluwRcva4sbCIoAgiCuvlwvLCC7z6+us8//BTYytnhubEs8qGnxJdcSPKuL8h'
        b'DgybZV+AS4zduVbGSpOG3TZaKnfRPF3Do3f+zfUvfo0fvgZK5GNT7iAqdP3ptTQAuVeB06zswndU4CPr'
        b'GsfC7RoUT42dotrefXsakm2rpnMyUI8S73RvKZl4PfPk5sw7iGWrnuOE2rI3oRlTRtCwObO3G4AFWB7/'
        b'd2TSvX60R5CgethURemDMqGYcip84rvf49WrG7wUWg4dcFelpDdaFMOsFRrirIJVuH99xe+++WXaW/8i'
        b'7K0HqrUBfe7JwbPb1O4GPSyqNguRmdz54CtcSji6CTu2CwaY9L4lLYKVSonA1ytXy8LJcDnAzGY8mvxB'
        b'4WZ+R9kz0h90bwz077XbWGf3QR5sSgk7QDmsCzhEpnGYlYXrPFNzpUoUe+MUSx3qz/Dr3HrV0FBjgeRh'
        b'lgY4Q5agRs9Iqo5MBWlhGVs9SxqdP4QDpJX7jxt2587sh6XGMGMH7gww0iC1RmY0LGVvlCv//MmPeeeP'
        b'f6EMhV2j4SoUFQc4CkTFjm5LJVYt5Lnx+N3/sF494m6XzuHEodTaAd2qy7F5nUO56wAJ7lvw5Oaav//w'
        b'R7z5s59SWCk06gA/3PdTlkPDG3mb4M6osKOZ0+Wdrt5DVDloEUCVR9JENy0KZNNuzmh9zCVnkr1KYlyP'
        b'hnNIuTf/M+MftWj29fLSs1t23LvKLjuzdYyzILaJIZK1mrIUyiHgXGU7THS7Tg62lS6EUyRN59IzH3t1'
        b'VFgf6O1k2SPuvWycxebqLpYL7n74Zd772yuc1GVAUSD6CRQJIvo9XXFznEohiBBLrSynhdO9O8T738ed'
        b'j34EHjwk4/ZZcvJLBHWetbXp8DwOL3z8S1/kwRduWKOMw984sXp4G+0bNjfP7j3ObjgNbn1c9AVkObFp'
        b'39G+jqZcjZBy8zOz0aahlRPEMh7o5T1XZu0gNku1gXXXqUhw2duLR+BZEvNsNuNEUKF1ohYNA9G3LifP'
        b'GXqzu7bNM3VyHAyeQQWc6t+U3RYf8jhDTaAzhBC1606wlBiVM7rwGNKpNbdlJ5kPkc3heoBiO79ruAj+'
        b'73X8r2nWbKUZV1hCLKK3Bx8BaAO3RdmCz0nn6Alt+99k/3VW1MiYRsjtYGloLam5nqnLPS7KwlKDZG+Y'
        b'O/JOuh3m7vJu6+2RR8NfbQTzvs5N9+ZlL4ZsSX3zr29yuv8+/nw6cdVEKZUo/R+KWw8Ptmue2yYRD5Mc'
        b'eTF267A9/S88TO+DmEBYhWzm5py89Y+3+R+HgwE0gNdMDQAAAABJRU5ErkJggg=='
    ),

    'img/6.gif': base64.b64decode(
        b'iVBORw0KGgoAAAANSUhEUgAAACQAAAAkCAYAAADhAJiYAAAACXBIWXMAABJ0AAASdAHeZh94AAAGyElE'
        b'QVRYhY2YzY4lRxGFv4jM29PTjNyeYdwGg0AWEmAJYVasYAcLtvAMiC1LluYJkJB4AsTKK54ANn4BVhas'
        b'bBmEB3vaeGaa6a6qPCwiMitvzyCRUt26t34y4+fEOZHX3nnn1wIBhvKMGcaLw+xlVxnPGpY/csq8qpxZ'
        b'yqN/R5h5Luksz6+ooHywsamBYuG+uPqHxYLxe1zA0qC8QrdZw6A+hLDdoH7VhBHrCaiYodaotXJ2egcU'
        b'VptP0ZDGRGZGj98w4la4LN8J42wYidlwUAZNu8NeClpPqO6F6+uFBw/u8/b3vsu6bNRa8eLpZosICJat'
        b'0Vo7Sl1xp9SCAVtrbOuKEQu4GZLymCPVnWxAGIYZnz1+TO2Tm8GyLCzLihCFkuZPBi0rTd0gQ03Ug4OH'
        b'l+u6si4LXgoVkBe2baO1Bmb4EQwUADBLHBVqqVQBTY04R5hFoyny3ZHYJHCwltgxw9wQxrKuI13lUMPr'
        b'vrQZ5h633Ueawyrf04rhXqhoz6WbxUQJbCTk4kbQlGjxwISPyE4YmcBKAhUHw3Fz3CJNRs6tCURpcOXW'
        b'MIwm4RJ3Kbz3+WP+8OHHtLXQcGSOl8CM5WS9sFvbwU8PbnPcnYLxy7e+yptnJ4GiNGhUaL5U3SO3xYxa'
        b'K6VUlnXF1PjLsyf85v0P+fh6RfIRWll4PerLwhDXzl9BEcFpMsOr8/fr53ztbsm7aYVsBzpQB1vBRFKG'
        b'aPz+g494dHUD5ulCVE3HyzibJ0MZpsmkNKafr5toJB0o7UkS7RxWOw4SwaiByXCcZQOZ77hoLRfyHZk9'
        b'd1ENZCUP1nYz3JyGs2WKTMfcZdO3WmvhcKiUWrJ6hRtIYlm2MLTXvTl3MH7wyhkXpwdcysBZFkWh4JEF'
        b'j6iAUdw4KZW3751SJgbXSJ4GwQYPmeHeMaFB49sgeRtTnJ8UfvbmBV85PeDWjenT9vAbnaF9VKFT3DMb'
        b'acKsN5nqqr5m6pk0pDBxlQsNGRDFLXDV9WzHdvzWjhG6uZPGWTcG9nMuVkNzAqzbtnGzrNRSkCnEdsQt'
        b'hqfB7XZH0IE6eoY8pyNhg7+0ixjFSgd1eqcWWkUpx5Z3NZR4uoi/PbvhWSuU4tRJ8RsagE1xwdxo7twr'
        b'4mHtnLVDgFtiXSOMMYuXwiHpfBbEfQLj6bbx2/c/im7AfNy1rOVZRGNBR1Y4LYUfffGcX3zjS4SSdKKY'
        b'UCqoI50J7JLADJbd+55OwZKxJlcNeh0gPIaFJlm42Rp/fPQZb52f8cPXXsW0F8JIa1R4VMGsRzYw6C9P'
        b'9AtN0PEI0NoAd1hnNIM/Xf4nhPp/jLpuG+sahxQY8qmCjgxxwwUHgbeWjNuZPp9LdW4Y12Kktefm83VL'
        b'tldK0FRxQG1NbNl4SUItFH54Og83zr3w868/5I3TQ6wvo6k3G6FgbuLR84Xf/fVfPMm2ZazaRmNyVHMd'
        b'NrWnKqLSA2PjgV0i4sHTg/PNV7/AxaEmsA1jG8lSa2wSD+8euGvwlEk61cm2F8GUAE1lP25oeqI3Z/Nb'
        b'sSSbDNwTe4ZZGS2EvDd6KR2djLrjWdE2Lh9j07OR3A81OlfvRu2HCTatbAhZtCLdDxnIo5NsBtsRG8eP'
        b'uUzmWPRzHQSW7YIloM28C/gEOvHpzcq7H3zC66cnQaCWjGKwCloTJvHvm4UnTaj01iVCEjqpXXJmGcCC'
        b'h0hG9VKpFlXTWhK9km8yDM8Ff768wuyKXiAa+bIBOTUxaLzD08RJScdvhyh7oxoT7O2kAS1kmrMC7hbb'
        b'FHZBtdk7srpGKFPdfcpWV3+M1+8cblWvhtID+NY23B0vzqYWOxBFUf70jdd4cKce9TYvOyzjb+b53TH3'
        b'3HDGUcw5N+cnD+/tAtrtmaqwqolSCtWdbVtp20YpJ7g537+44FcnJ7z7j094vio6yDYBs6c75ysYHk0S'
        b'DacRVXgozv2Two+/fI9vv3J3VN1R70embFwhBHVTo1juz7zynfv3+db5fdT3ZkNqe+I1cDPcTIzI9vQW'
        b'V4iq7eI9eRWVrY4hI/ZEpeJe6F24WfdaKOMy94/diSn6HVGx1ISz/n3+y2B/K/qx1pQdIxr/eDiGuiqq'
        b'Nwl7aR/NM6XteP4dykfZ7WVpe3RH7pLla2BAmDamBuhodD4aNsxh6unulyYreuH1Hn3ahs27rzGaRO0K'
        b'r21FbY2Adz0bTVf371YkXojA/3FNu6FHcwpaa7G339m64WNHavny/mdSz/W+2vGSYk7xfH/fNoyGNRk1'
        b'sOUIY1s36tWzp9ws1zy+vOTePx9RaqHWA+Zl8MjO7y/6fKTBU9hum3r7EWk3UWYI59PLx/wX5327ASuz'
        b'2dgAAAAASUVORK5CYII='
    ),

    'img/7.gif': base64.b64decode(
        b'iVBORw0KGgoAAAANSUhEUgAAACQAAAAkCAYAAADhAJiYAAAACXBIWXMAABJ0AAASdAHeZh94AAAG+0lE'
        b'QVRYhXWYXW9dVxGGn3fWOieOJUoVhEOrhJaKorQXcEOEnFKQoiJuuCJBqOIWqbeopeJT4poLQP0H9D8g'
        b'tRHqD4AKJCRoQXHtNnyEGAlScBzb5+w1XKzP7bRbtvc5+2PNzDvvvDPL+v4Pf+wWhByCgWRIQgIhXJRD'
        b'KF9EgPqf9qzE8J3yB3Bw+jpI+XkDl4GWHK+N9XREjFE4IFJ+2CeQlXeLE7SvzUa24MWQyqVsyL346uUJ'
        b'd7w45Tju5aaElB2RLfETJ9b1ppWx2BAWDDNhZUWfEg6YVeQ0886rpYaG58/FGQMwMBlU9EMghPzZFPJr'
        b'q4l1mIgyw3HOb53jqac/0yJp8Uogp1mVDTDVNHXH8nl0snnX0uYNwpJyssP3Dg+JkjBg5QnMWgI0Tzxg'
        b'jTcVJYfy2cuy4PKeKkoshXjjcl7RpGZPTGuIIYjJwULAXcjyy+YZFQk80ZFpkZHTKsDzPa8cc3+AayPT'
        b'qsOuzDfkIMciGaFGSbMSjBNiIKyck/Uxk2KhhpeQyztWzgPxHct8wQsAjk+OkzA5MgeFgo6a4yoQxpGP'
        b'GQ4nAfeP7vOLn77C7u4tCPWWD5LAkIO8sDeNcJInvPJHwiywXC556tLjfPuFFwgman1XarpEJHmGD7Vy'
        b'dE8cHB5x6733+Nvf/8o6rUk+82BIRz80u+xARkrFAhir1SFp8haU1LXPgVhRsVFv6m8oBPKE3AdjtXbm'
        b'sM+dAUiVDFQVCgJXQgoDz0pl4sSWQ4EnJ9NIhBAISzEx5cppdeyNMvoQ1GpA6QOgXISAmZoMSF0wca8I'
        b'5YrJEGZrmxsbXL92jZ3dXVarNev1GncnTfnF5FNX3+S4Z7ymNGFEVkcn/Ontt9jfvz3kVJxZLgp3KumF'
        b'Fb1yVJS6ONJ6UUHoypVn2d5+BpmVlnCaNHXpCl7K6hsC67V46bvf41/7d4DUqv+hhz7S2st4WLEf+4Xi'
        b'VDEkBwuWNagaPJWCStXuYInTxf6dfW7tvYswvCRPcj5+fgtZaP2trlYJERtJB1LXJ4SyZnTRn7nQFmyd'
        b'QEwpi+xbb/+Z4/v3Ojr5NhcvPlrWqS2pZiY/FUcDXUnnIl+J1+rJIY3PNAU3lovIH/74F1795av4tBoC'
        b'yIL55KVLJdjqjFpHc3cihYxZB7xFUpt2Q84dyUpjLAI59Ky8uPHOu7f4yY9+wMnhfRxDBSGZ8cjWx7h4'
        b'4SIGpNGZxl+IufyzUmjo0KqGqoSMx6DIyHLfMyME48Zrv+b46JjJJ2SOp97HLn/+MnG5pBZOF4jOgei1'
        b'/IqLzX6FyTtqGaXhXm0ZEmbGwcEhb7zxOj6tye2jKLKEMfGVr30VKcxZPPPHiSMQo6fzCxUNNYWuo44j'
        b'goyjoxU//9krHLx/QJVEIYJlKnzus0/z+BNP9DHpgaPoUJ/4hhbQEBiccWXdqSVl1UcxuXjpxZfZ27k5'
        b'hO4IY2GR69e+zjeev87CzuCeeJADWRLEDKHG+5IatYLrg1g9F9ctU/q1X91gb2eHdZpaAI4jE489ep7n'
        b'v/VNlpubeVoorpa+M5uRhGM+8KRyZtZf1J1oS5RObcpT2Y0br7dnwXPvU24Jl7e3WW5ukDcRc+L08bzO'
        b'M3l6HSI/ndXyct1CDONU/f7Pf9zm5s7N0la8tQhJLKK48qXtFpDKhDiXin5PlpnQSForyEeTQ9l3jGpy'
        b'jd/89k085ejrhFhnnEfOf4LHnvx0e6M58yCFmuxER2ichzwx4lE57D7yKD+aUuJ3b/4euZNSag47YIhn'
        b'nv0iixBJKfXt0gcIm4ZEWJ+HND/XPDfC0fhlgiBxeO+Am7vv9HFC4MqKvhEDX9i+QjpVVHlMOY1SF8o2'
        b'U5tpXkGtjbQ6KFLfh7S9vV3u3r1bqiZfNwzJ2No6xyc/dbFv6eiF8mE6VMYPb9ringrP6xxcIB53o2Xf'
        b'lYBzDz/Mc1e/zP/++z7HqxXr4xPW0wlR4upzVzl7dhOm1Def3o0PHbvlzRSqDuU2WOMYCpyyKevl6NVH'
        b'58KFC7z84ncy7yySEJ4mTMLiAvcaVuqvqqc/E6b8epsYhwprW5dK3GJdPotG3rc9ppAdqSwwyy6kaUAh'
        b'F07rNw8kq5zNiJWQuZJS3pK05b1xY65FfR7OJLfeUtrh9WfWiKsKdW46ydW23HVLSgzVkQpiV97RUNWg'
        b'sUhmc8JMIqoM1ELIe7+WkQGd7I8RSQmCsQgiiJLv/s+D/vgc6tr12/chYmvpHoxqZnpYv9RecqYpEdfr'
        b'FQvbYGlGNGU+eEvYoEd10bF9FBeqkquiMZiaMbnfF2WAKOWS3ElrJ969c4d49gy3b3+Ue8cTFgIWrHX/'
        b'uqN0d5Ln6prKjiH3UG9znCz/Yyujb3mt3EcwCwOKas87kWlyTo4n/r3/H/4PzuSieJ7hC+UAAAAASUVO'
        b'RK5CYII='
    ),

    'img/8.gif': base64.b64decode(
        b'iVBORw0KGgoAAAANSUhEUgAAACQAAAAkCAYAAADhAJiYAAAACXBIWXMAABJ0AAASdAHeZh94AAAFnklE'
        b'QVRYhY1YbW8bRRB+Zm/PsePESDSfIKIgUfEF9SfS/4iQGlQhIT6A2qhKlLqm9t3t9MO87Oz5irjKyXmz'
        b'O6/PPDNb+uXVK2ZmEAgMACTvAIEI4ZFVNGv/72EO77M1BoGIkFKHw2GPDGYwA4wCZgYDIFL1apH/JAY4'
        b'rokCiqoWlMdd0SMJAKEwAUxIRMiygZFSh4v1xZkQM46IggpqLJoFUtY0nGQOEvkHIDAzChikBqWUMK57'
        b'ZBCBGbje7fDy5c96KHl6zjP0pZzNQhO2ka6x/tOUoHDNCpjw8PCAzCAwilsOENiiw42aKnnBSI+fg8Qz'
        b'7qmBIZXEJmKqcAChz72lTAFMFISqNwig1NDHSBl+mlQbnBSQMdo8Rx9Vo4gI2QWR5UciE3wThTEw5NLP'
        b'HzZzLcoMbuvBK5qoxQQRIVMQRJZ7Ej+4APv9Hm/f3ePT8YipFI01haLiEKkaOyKpmpQIKffo+x5X2y1u'
        b'nn2NrutmZ0lTTMi+gAKioIyBD/s97l7f4Xg6VZUWRc8DNWmq7wJeBoNZIkEpIaUXuLm5aSLKhk0CUhvv'
        b'mk8G8P7+HqdhMCRphVTfbL3KDsbEeAVG/fjx4JXFHKpO9+Y2zPYmG4Zx1K/CG9WUaLZUZS3ACvCaxlos'
        b'U5FSXyIPAgKGUMFmTynSRoQY5EDXJTy7uUHXdY4Tivyg3o/jiIeHR3GKa/Tts2QMCMhEMTIKIbYKsOOM'
        b'pCXf9xk/PL9F3/eVfV0sO4TGccKvH37DOE4eUwM73M1ZahHKvvKLvDOg3jc+iCDHyTJrO72WUpWqoC4l'
        b'l0n1xSOcPEnnvbHxPq4LoMmBfU5HcqqEiNmmnLP2xro1ThHZPaL2IAHYrNfVCwYKBJSHwwGnoVcM6X5n'
        b'Z4ncOA6eLidlEDbrdaWOWdLcIG8JbJIlMre33+Lp6QnvHx7dg2Ec8frujbJ1bRzO7qyx0+bp9AygzxlX'
        b'11dAhEf4TQBS0zpiZ4QQ2eXlRrYymhTZp+g8Jb85/M0GvSp1ddEj99lV8Lx5A0iL/Sg+HIQGwDDDuWkJ'
        b'f2ZUCJBz0Dl5WlAgVbZU5syMMk142u8XbXbAz2kDDBRhrmKEqbJPpwHDMGK1SgsS5XSWGj5XyQD+/udt'
        b'NUgNWK0yfnrxI7rcqTJW3IhAY5lxmnD3+xuchtFljtOEw+GAVd+joqd9reNHmG9sNDieTm6MpSelhO12'
        b'4wY1E0QFJMo0nY0XDMLx0xH8lTWc2j0tkNkEWS9itwiYyjRTFNsvmmqJnpKSCxM5XxkYhnGQ9jI/q+fS'
        b'XJh3cmaUqQRWrl54qYYmSYoXY2koU8fJjgiYprLohG3Izah6ZjGE/pWjmIBPxwF//PkX+twhpaT9DGEk'
        b'kpdxHHV0oUYnM1femykjALkZTWN/IkLXJZPip8Yy4e2799UzVpeatPLs+iQbCUBK1GBrTpEVQ+FSKDMw'
        b'Y73ZtHwZXPH7le6NCqw/xinAMLrqc6WK0KbMo2QUwqhMa7u2l5ealiCdasc3cpz3QKCOJRFbXSLsdtcy'
        b'a2uDjZlj6DwUHFRv5Ntud43vn3+Hw+FflFJQSnGDav+LoCXHlPFRSoScO6wuVthdX2F7dR0qlbUKVSdz'
        b'GGGbUUM2dLnD7e03qLNyeGbY8zYS9hpWksEhGMsU249erUuRKrOch2bfes0UrgN8Ppsx1ZvD3GivkXpT'
        b'iX2RUIMsBnl75kaQsPVceAQKNeuC0bbEEbYtfJHjYY5iSRmDuYBCpBS2QU6g79ju4/cldRGw3grsD4xi'
        b'NweVVQxDzAVgYVX/b5dZeGT1S0D6jxnmjG+qYTbIGd+XMsk1iCD1nyxKNGPXINtj0hDjgh0zTIUOqMcM'
        b'RFr7yu758fERUxmwucjYXG7R54zUSVtIKVW2bSIWU/iFCKlBVv5WudYb7dbKTGBKQOrw7v4enwHpD/f4'
        b'4y199gAAAABJRU5ErkJggg=='
    ),

    'img/9.gif': base64.b64decode(
        b'iVBORw0KGgoAAAANSUhEUgAAACQAAAAkCAYAAADhAJiYAAAACXBIWXMAABJ0AAASdAHeZh94AAAGi0lE'
        b'QVRYha2Yz29cVxXHP+fc++Z57LHzw6kCWAmN6oAgC0BdoC6KkEihEkggFcGCCgloK4pYwBbBjnUllkgs'
        b'UCVQdyz4EypViBaoVAUBaSgtiYjTJkoc2+N5c+85LO5747Eznjppv5Y9fj/Oud977rnfc+7I87/8lQcJ'
        b'7JiSxEluWABQEkJ2IYliEkAUV0FFCBLAhGRGNgMxgioeFKQHUoEIbo47uAOeMAcQ3AUN0v4fiG4s+xZR'
        b'vQGpWI6QBJIITiDjOEJGyaEC0TKAAEB0Q0NACIgLWZWxjMkBHAEzMgoq4AIOIj0QcHPwRLaMSSBVEWLN'
        b'8dGQmMyIIXFiOOKTb15iKIG7UQk54QhCD3WHZAgCmglZCSrkWomm1KPMnV5mRyqiROqccYwUnJgUPIML'
        b'AoglMMOCkoNSNZF61KDpNv/Z3SDumFIbrP/3f3zzpZdQDBy0RHYP3n5oue0ABuIwBt6M5f66QzAg0Dop'
        b'kMyU4eRjcmHAK0sQG4eIE7Y3ES8DdAYyyzi3z9r7BlwGvpeUNZQXJdFzkFTeCQfmNSF44DoAtgUxBicA'
        b'TTREHHxvwKMgA1eAP4tx0p0bwNn7sJ+GAzEIqCi1G9LGQg44POjcp34FWFbAhAZn7PtW6r6IhQDq6phA'
        b'sF7JiTlOpokYkCgRuiNAEDKBHGT/Et8HTCAagrkRPM8kYsCr0uevPmQE3EC4TiAB2zibGG9lBzGGwHey'
        b'cg5lHXiMzBeAY5TEr9kfvXvGMojm4CKElk43u47cHeAbPuZdAplMUZk0SWppSXeGr2O8PvFQcZbAzxmx'
        b'hPMKNV+j4clDYmgG0UUBwWSPzDSpHWBb0p4UTL3jcOjyCI6SuEbiZwS+FOGfKaHAlw+JlDlEcUUEnFBm'
        b'OkUmtxGSVie6wXVKTw6Dt/YAN8n8ITmnRVhwn/gKM+yiipTZuJCnmHcON6YIOqAE+nXFR8+dZtBbYPv2'
        b'NlfeuYb5LIY+idUY46rDLYREkZqDhCqg6Ks76jaJ0HQArgOjqevjgwEv/u4Fzj1yHgWaJvP00z/mjb9f'
        b'mhsrb7PyL/QYMaJmTzS7fI1lwlqKqcokQbuXlCJ64yn3g8WatfXzpGqBuzsjTq0eY+2hk4eQOQjlLYp4'
        b'zsq/AGhyJYuSrWNYSI0pOnP9gHFU2Lp9h9HdIaNGWFkZMFgIpfDORfGwg7PR+rYZb8UxgUqdfjMiC6jv'
        b'r1M7B2bSWGZ5eZHTD51iabFmoc70tULZS+LDYYzp8a86cQpnrYHBlPMeEEc5UEXDesobUfi99bjiJQl7'
        b'kniNvG+kqzdu8pUvfoszD5/h2PIxUtrl1df+hh1Jnx0Y8WxTsYBzxmueI/MThmhHKHkgmbAZl1ly+GNu'
        b'+DegeCt/92Lj1k02bt2ibcU4ggrsi5J5ww7KZdnltz7gOYYMKOmihtDkwCgFzmbn28AFVVapWZ4r9j75'
        b'OysX5kMh9PGwwqdktG/7R/GMi7Dou3wc+AXOTz2TQ2bD4UcivPz+yXFEFM37rFZ8Nwy5YEMecaNqnzoQ'
        b'8YxoJIayywCOO1iG48BjOC9/WHwAQXnKGp5tnB77G7gMaE8iQWPpfSdGe1v/4Q+RDICirLdK3ZWQjpAA'
        b'GnBEIn5A+jtSj8IkpB8cwooon259T9fHCWFtz1lCmDwVyvItABeAz0/ufhAoxMDjwVinbPGK/VsmA1qq'
        b'vWAa9o3ZkVoCft0TPlLNa63moStCgaiBH3iibn13laGDARoDKIbKrGagYNOEPuWgeH8oREChqrloNRdt'
        b'foscxcueNgkz1c2BF5LxHoqiePsj+BwxlCnrihCXedKH/EY26c9R0F0gihStNT18SZ4RWPPMuwTuoFwj'
        b'cBNji4pEwyaJvdnUKH1WRfgEyuPe8FS6xecO1f09JIWotKfDOPt1AZ5wuIjjJAzIjBkBuzS8F+GrWXjb'
        b'BUH4fhV4ZnyX854ZUJL3qAs9FogSDNVMnFMAppuoQNkdC5TTxCpwOsA7uRwUns87PHpEAvfAQIVEJNFL'
        b'4/c3mMFUM6zhCEpflNUHJUP5ykYrRsTgjMLuA3goG++JDKeqPp8Ji5y0+6n8U5DyjU+MSekNIr3mwXRG'
        b'BH7o8PXeFgvJWX6AQHeEGod4Im6RF1ZZ6XrYdHQHXSMkCh8b+dFtZ8AVFg3i1SuXqTY2+dPwEm+fqEjb'
        b'5RBmnhFzRECRSWOt7riWTVm3lTGLMFZBxOlnx6XsGG/n1wVNALdyQjUBVAhajmDb4vxD4f9CB8+bRomK'
        b'LAAAAABJRU5ErkJggg=='
    ),

    'img/face1.gif': base64.b64decode(
        b'iVBORw0KGgoAAAANSUhEUgAAACYAAAAmCAYAAACoPemuAAAACXBIWXMAABJ0AAASdAHeZh94AAAK1klE'
        b'QVRYhWWYe/BdVXXHP2vvcx+/R4Kk5EEJEh7BEBJQ0ghFSPARrJQxPlqxvoABHWXU4h+0kNCp1VIZQQUG'
        b'GDFjLbVltI+pigKTQtEWMTgiIg9B4EdIYiRPQn6Pe3/3nL1W/9h7n3N/emfOnHvO2Wef7/6utb5rrS2b'
        b'Nv+t9QZ9qkGPVtHCOY9zHnEe5z0iHhEAEBHELJ4RwBAcLj3H0oGhpvV/U0NVUYsHxDkQMANTRQcDRkc6'
        b'LHzt8bxy4CDF2Lw2Z592FqtXraTdKnDO5dlxAk4cTiROFNFFUAIgCXQEaek9anxCcyM+NYvjzNJ/M0JV'
        b'MTXdY/tLO9j+wvOEqk+h1mLe/NewZPHRcbq4BLC8qoaOBtDQ7QQmkYOlAfkaEWq8kscwB1hVVVQVHNyz'
        b'n8nDkwwGJYVzhvORFec8lk1gc+aqP4jEj2U4hmAWR1hmT1xkS5p5wEAzY4IqaOJB1fHr517ixe0TVOWA'
        b'siwpBMU7ECeIg90797LvwEFAiZ8XLDmRJhNgCgIKBIMABHGY+MirgLfkCiYILlszGUXRYFRqlIPA4X37'
        b'eeaJbVQ6C2ZUGig0BCQxYAaTvR6HpmeogjYrFZeY0ciWGUjyKOdq71IRTCQZPQaFx8Wr5G+S/c2MEIxQ'
        b'KZUp4gwLNXIK04BY/QriXOMnaQIjoGaYCZYjSQBRfNmnEMUIECpwhrk2wXUxKQjiIMKsmZP0cVMFC0BJ'
        b'5F2jpzihQAwZ8k7nXP1iXpmqoghqhhpUIaCzPfbv28+2n/6cXz39JPv27KLXn6Xb6XLUwiWcuOJ1rDtn'
        b'DctPPoFAB6RIBmgWHT3XEEKmEkPwGIWaIU2wQVIoJAOx6EdmBIXBoM/hQ69y9z338aMHvstpJ7zC+Wcq'
        b'K08yFi7yhIEyMfErfvbYQ1x31bdY8roz+eBlF3HKycdj0kFwkflsNSwFXBOuYlCo2hAo5gzAYuSoQQjK'
        b'YLbPxPZdbPn6zZy76ike+Y6y8nSgkz0hNEEYBkzvHnDXP93Pzdf/ghUbLuPDF51P4QvEBLMm3k0Dw3YD'
        b'cBF67WKJ4hzGUcFVA1U1wxNPPc5dd17DbX/9BHduUU45G2wcaAFFPCQfHRhfBh/9m4pHHtjDqXojX7zx'
        b'qxya6REoMatqsQ0ahiQpOrEza0jKQZhRRpoNDT0ee/xR7v3uP/CfN+3jgneCG2OuC9jQeUhQpYDx44y/'
        b'u2WWS8/9D75yw0280p9FqcACploDy9nEAFeniSELAtG/gBBKnt/+LP/2zzfyL9cfZsUZIKNAFeUMi/+p'
        b'6sBqzsNC3YHLryzZuHIrW267nX7ZRy1gGggaalA5U7gMqgnEoXxnynR/kq9/7Q6u/vgMp64xGIkfNWBQ'
        b'jjB90GE9sEEDzgJMzYyya6dDK0kKHMFdfW2J7bqbrfffj5Z9TCtMtbFYik43nOvM8kJzoi3Z+uADHDX+'
        b'PJd+SKOThzh427YOxy6fZeEy4dt3HYGVDYOTr3RZtb7ktacaH72kjZVSM9leaHx2U4v/uvMbHDiwj6oq'
        b'U24a8nMSY8MOZhiaknevP8nW+37AJy5TirEAqfCwCu75d2PfXqUfAr94wVEm8cTgwG9hx0SJOeN/HwsM'
        b'ZlNwpOfrNgxYueRVHvzhQ5SDGdQ05g7LQ4TCso4lNY9HzI/PvThBf2oXF7xTkXazIhy85a2Ohx7rIK0O'
        b'b17Xp+20NsXRJwQ+8I4Ou3/rOedNFa3R5EOSWOsq77pQ2HL3T9nw5nVUWsXMMhQ/eR2RLQNNEwQ1nn7m'
        b'WVacFJg/DvgGFArnnd/nvLMd5g1plbEMSsA73ZJv3krMsWOGS5VFBi4OTnuD8PIdu5mansIVPka/xZg0'
        b'oLChCxguv4z9+w+y6A9ipdA4ZmQXBesqrhg0a0umlgC0gUJJqXLIeeK7Cxc4wmDAoOzRKcYJSchzyRkF'
        b'VqTOj2KWypKAE0+37ZEc+vnnE9c+J/N0L4Gw37kGGvlI42dLxXvB+wInLueAurp1dVogS5uhGuv0JYsX'
        b'c+hgC/Np4gqshEEphJxRqlQgJO2qhdKDpdnDrCeUNLqmsHOnMtJtM9Lt4sUltY6qbxiuzlA5KJKWiThW'
        b'rDiFXz83wuSUi1IQIBwWbv18wa6nOpSzsdKxEKXCQjSjGLWeHdxTcOXHPfv2+oZFEx7e5ll69CJGxkZx'
        b'vkglUUwlYpZjnDovZcuIOI495jiOXLqa+35QUGl84MeMNSvgM9cqE0+2MY0BYxI/qpkphZm9HTZtdows'
        b'rlh0jJK/NnWgzX8/6Hn92jNpFSN453NNU5ftTupwyT+pWe12RtlwwQV85SZPOfDRHT2c+56K954feO9V'
        b'cMvNBY//WNj9ovDqIWF6Rtj7csHWe+fxno8FDpYDNl9rSBFXbRV8+1seYyFnn7OOVquLiPu9hF3U0dJQ'
        b'l6pIKFqOM05/PT/cupZv/uOjXHr5NK0WuLbxF1cY7XkD/vLvPVd92SMu4IoW4NBqQHt0kndthNu/IMyf'
        b'b3UPueelEW67A97x7vdx5IKjwPnYjSWRleTOhWBNQ5tAukglXoTRdpsPXfIRvnzDM5z5hpLVbxzERqOA'
        b'P7sE3vq2wP89XPDsb4zJqYqi8Cw9xvOms4zlyw3nm1VX/TabrilYtHQtZ523AVd0wLSOyiGjUUjyKovm'
        b'RTXW3U4giOHEcdwfLuPPP3IFl195A3fd7jj5jD7m4/gFx8LGi6okBRrXO6fyTME76PL5zR2eeP5EPnXN'
        b'FbS7o4gpZh5xQ7qS3MhFWEJTZTS1uCN2Q963eeMfredP3/9XXHhxh+/8axvrDfeZNJr1O6AADh0Y55OX'
        b'Or7/4PF8etNmjlywOPYWIoi4xsfSL3X/UkdE3GOw9L1c7EbhcTjWrDmXT3zmOq6+YRkbL2zzo+85qknX'
        b'SM0cmoTp6VG+sWUef3zGLBN71nP1567jiAVLcN6lrt4ncFL7kYggzlFk1JmtEFJdE2uiKJAWm11wLDvh'
        b'FD57/Zf4n3u/z8Wfuoeyt4dVpyvLV8LCowTfgsnD8MzTwk8e6jE2fxnvv+xi1p6zHidtMEHVUt3fmJrU'
        b'f2KRsUKIwJxpUnytO5BsIZN0SwDn6XTH+JON72P92y9k4rkXePLxn/Poz15ievIQasrI2DhLj13Kldes'
        b'ZfnqU/Ht+WAOC7HrcjWcmAZNc67O7uEowKVeElBFqxILFYSAmdYNgpH3GpIvOqEYGeek1adz4qrVaREh'
        b'FiEuea94zAQdBMRCzB7iUMDFThWT2IHN7W6hUJM4oDImD0+zY+cO+v0eQStUNfaUIqgITjL9grgCiha4'
        b'uC0g4hDncz+fKpDYmhECqoFQBapQoaGiqipCqLCyot/vEzQl76T3hfOOfr/PxI6dPPLIw+x+eSdlWaIW'
        b'ErDYwoW6YYnUkwI4VsXSbIVJE6QOUvR5DBdlQVyzp2ak/lLIwp4nKcbmzeOXTz9Fb2aGyZmpqGOS/MvF'
        b'MHY4fOMV5DCsuyvL9UnOs1Kfmy0rmkKu3pjJGyHxRZcqFsFRtLtdpmYm6c/GjgWrGvsPRaaazVlTLm9M'
        b'0rwpfbgamGSUCUAUoJxmLDu+WN1cx0CIelAcOe8IIFCVY1RlSB1yAI2yYWn/IjOj2YY1OEEtLUNzXQfD'
        b'26GkcTQeGC/rTZt4BFVCMGanS4pemSJJHa7IqpuF3OrEWhuk7paFZitUGmbIai5zLGXWeFFUowQoBKqg'
        b'lFVFGQLVINDr9/l/+4V5dHwQBDEAAAAASUVORK5CYII='
    ),

    'img/face2.gif': base64.b64decode(
        b'iVBORw0KGgoAAAANSUhEUgAAACYAAAAmCAYAAACoPemuAAAACXBIWXMAABJ0AAASdAHeZh94AAALeUlE'
        b'QVRYhXWYf7BdVXXHP2vvfe59v5KX1/wkkmBiEoMQExKg/JDywxIYnaIypjMIbYri1DrT2o6ldYahdaod'
        b'UIvAtP4YHcXRUqrVomGQsZXIVI2aH6QghZoxNCQheXlJXl7u+3XvPXuv1T/2ue/dF+S8Oe+ed985a3/P'
        b'Wt/1XWttKctkzguYIGIgIIAhCICBASJ0HTbzaSgGJAyt7jUMZ2QLJog4RAQn2eYcU+dYnZxq8tjXv0Hw'
        b'Id8qMrscHVD58jcasgpCMiNiJEARVME5j0Pw0jlnbcgcG/mXmlHGxNRUm1OjYxx8+RihA8HMSO0S7Sxp'
        b'hqqhqqgZMc1eJ0vEGEmxpNREmZQyKVENVfA+EIKnFmrUi0BwniCC4DBTVJWUlDImWu1EKyamJqc5OzrG'
        b'sUMvM3z0EGEGvRq/3P8CzZRwoUCc5BCpkQzMQE2r05j5MSOpktQwVQzJNHAOLw7vfAbqPMH5HAsBBczy'
        b'vSkpZavNxHSL8ekSQq0LGMZkq0UpQkqC4Wa5JDlMmFULK1gEjYhVtyUlxUQ7GVp5xzuPDwHvFec8wYF3'
        b'DicORCpbDlUlaiJqJGpCoQuYGXgHJph2SG3V/ySHtgqjaoSypN2cYGxsjFNnxxkfnyIlob9/gPkLFzNv'
        b'Xp1a8BQpUPiA8x5zHvUO7z2Ih8q7ZmAk1CKI4r3M9RiAJQVxlXeoHlJMjbJs0WqOMzo2xu49P2f33mdp'
        b'nB5mGaOsXNait18YPeM5MLaU/qUb2HLlFVy6YQULBubji34kGEK2LS6vkyOTIZopOQTdHlMABySovGNA'
        b'MtCU0FTSak7xi+ee5TuP/zODxWHe/3tttl5vvPktUBsAfLYz9uoETz91kK99cyef+8lV/O4tt3Hp+hrO'
        b'KSIBMLwUiGSeSoaVpURclic1MwGazRZ7dj9HqUo0I1rWpTIpMbYYb4yy4wff5vgrT/BX26d55zugPjQT'
        b'kTkSMKNnDfjpE8Jnv74QWfEBtt50DYvm9VLzHu8c4gKCR8SRUqQxdpbhY8d4Yf+eyo9VVoqAmZIsS0Oy'
        b'SLI2J86M8Pjjn+fihd/lyS9N8573QbGo8vc5IieAk3zqIFyxzfjKg6e4fuAhfvjolzl6usFUbNFKJWVK'
        b'XVne0bUcStexq6ogUqWxkjSRrM3JyTM89d3P8s5Ln+Fv7m7zWytBivzg6ym4VKSoAVKH2nrY/rEWf7hx'
        b'Bzsf/SSHzpQ0Y4uYWiSNleR0WJ7Xn/VYB7VU4iqRRnuKf/vOA9x0yV7uuh2KBWDF66A55zCyVkHOpWII'
        b'rr3T+KPL9vHjR/6WkalIu2yRUkQtZa+JoJo5PkN+Bcxlk0Yiaot9//00q/p+wQf/IIdFahn58HDg5IjQ'
        b'aEC7TOCEojASjnaZM9gr1L2ydLFn2XmJWAMZgBtug2cP7OPpHY/wrnffRfARrwVmnQgYIbhuucg10zDU'
        b'ShqTDfbufpyH/1KhN8fm2PGCu/8adv5H4uxYoF0GsJxlzinOC7HsmMz2BnoTb11d8IX7lXVXtYlL4PY/'
        b'hifu/D6/3vx23rp2HU5TVQUAU5xjNpTMdAdKmdq89NIe3rjuCAsugLEEI6/Apz5e8q1HS06OKO12G2wK'
        b'mAKmQVvUepr5munq+0kmppvs+p8m9z6UiM38goveAls3ttj/ox20VIiqJNXsHstpMAMsxxhUjXZZ8uIL'
        b'e7n8akgRxofhxPNw8GXpJM2co17AB/9E+MTfB5Yse+3/BTh5EppNSE1wChuvhQP7n6fZmCJpmqksnRRw'
        b'3QZMlZSMVhk5fOIES88WhKNw5EXwA3Dj1YLzc9PRA5uvgHdsMy7eHNm4gdekawBu2KrUe6Bsg0zAilUw'
        b'3TjLVKOBae5kcik0ENcFzLo6hRgZG5nggS8Jn/wCjE7BGzfCHR9S7rgVRGbB1eqw7faC5YthySK4+QZm'
        b'9aJy19ASeNf2OvUBGFoAAy34zx0Q2k3ajYmZ9zCMXN+7aiWWqa8pgRplVF4dbfO+m+CWbVDrg+jhH//B'
        b'WLbYs2NHYlrhlm3CtlsjvnLNe94Lx0/Art2CK42FKx1/+iFh80XtjDdBbQjiSM7gmjUIImina5RMl1lg'
        b'nU7KBItGb38/113t+PDHlHqlXUFg3vlw/8OJ+x+AKIL3RkygVSb5fvjUfYAY5kBCVjPJ/To4sEHYskX4'
        b'6o889YEBvHPZQPYOqVvHwHAC3gmhVrBy8QrWv/nXWAEqeVHpsFIyuYqKqEWnXnYlhrzmIl+bQHLQ9FAM'
        b'zGNg3mKcy31ZdxF3c58XvIOeomDd6nW8uM+TdFbBO3I+k5nVoh3KzZzdf/yGw4ADhxPLz19J/+B8nAs4'
        b'53AGTgQ16c5KwTkITqg5x0WbLuKXu/o49KuqW+iAidA47Jg4Xofksxc6mKU6qe5XsDTXkxg0xzxP/gyu'
        b'uvZK6n29SAVMKpmHrlCK5FA6B0UInLd4KWs2XM5jX97JvfcZRb2yK3D6hPIX97Q4Mglr31Rj9SplcH6i'
        b't8/oqYO1hfa0J7YcN9/S5sKLZp1nSdj1TJ2p6UF+57obCd7ltt0JTiCpIjKH/JlfIob3jhqOa264kR/8'
        b'63M8v+cMm9+WCAIEWLUJHv504ItfM57ZW/LTfTCejLZmgwM9xqZVkQ/cBmvWzg3h+Egv//R54/btdzB/'
        b'cAjVqncy8hSVFOe6amXuowwnOaS1ULB80RJ+e+u7+crn/oXV60qGlpR5RqzDBZsj9210TI7D8LAwfMox'
        b'NmnURFmxEt6wXOibZ3PaI53u5aHPBBYtv4bLr7sZTx8qgiPPFBmIQ5ycC6zzXiDOEWp9rF97CePjZ7nv'
        b'nif5u09D31A5s5J6pWcBvGmBseYccs8lFsSyl0cerPOzF9bz53d/BO8GUDXysG3VpJ/TNjg/tyQJs29o'
        b'IggFRRhk86ZrKefdxEf/LHD0VzWI2fWOXJLOPeZkKMKZk/18/J7Av++8kA9/5F6ktgDtzvaq63eV2Hkf'
        b'5pYkV21QiFSuFQeuThEGuWzz9cw77/e58/19fPXhfkYO9WHl6+9FmAknhwu+8cX53HojvHjgOu766Ceo'
        b'zT+PhFRz6uyTgiAuz67eh65G0TQ3a5a1QSrFVBPUPEUxyKYNV7B80fk89u2n+MyD/8vFWzyXXBq5cA0s'
        b'HAJXQLMFR4849v9c+K8fCsoi3nvndjZe/3Z86CXZrCRYHjLoCI5UnvPOIWZ5chw7fZqDBw8wMTFJu4y0'
        b'YyLGkpgSSROqCY0RTUqpkVePvMpLL/0fx18ZYXy0wXTzbG7PQw/9fUNccP4buPxtm9hw2cXEnn6MGqKC'
        b'aGcTIY9SZrlwY8b46BiHX3mZY8eOdM+VWdKlirOT2TdBBJyHIDgPdelj9br5rFpzIeJcnrDUcOKo9fRQ'
        b'9PYSemok54gSMK2G3M6ZJ8eKNh0uWjXcOkQquTADLSNoAkuIKaYJVxlyM5nsszaLw0RwEhBXw3lP8A7n'
        b'XVZw8SStCrNItWjHU3RVdOg09ZjiLEvHHB2LZSsDSxmgVCAdipnhq+JqnV5LHDhBnOK8Q3z+Kr9+XsxU'
        b's+et05dKle0dws+GFDUiKTeKJgQzKDVx8tRxzpw9TatMJI0ze2Mz2UneQhJxM4uDIpLyIOICIh4Rj1kC'
        b'SRgu867j8Qq5VLuNalrtHIFGQ1PuxcoohGNHDnN85AQ/efJ7jDWa1EIuTU4kzwBkw6kCaGTxdSHgQ4Hz'
        b'HucDIQScD3g/C7DjQqvkg2o/Ladb/syBqTby2m1igtRsEmzsIH2pyZVb1jI9OUE75m2BnC2CSZY6xWHm'
        b'iCaklDvcGJWUEjElzFokbWPtLDGGYOJnOOYkt1TeCy5IRY2Qt0chN5tRaTSMnnog/HjX88TQS7AW2k7E'
        b'pKj4ihOpClkWPxGqzwDikYpbHkPEUUhnQ6XKMwMRnWnbxTpTlhCtGn6qs4xKu+WYbpVMTEzx/7GxVRWS'
        b'P+9gAAAAAElFTkSuQmCC'
    ),

    'img/face3.gif': base64.b64decode(
        b'iVBORw0KGgoAAAANSUhEUgAAACYAAAAmCAYAAACoPemuAAAACXBIWXMAABJ0AAASdAHeZh94AAAK7UlE'
        b'QVRYha2Ya6xc1XXHf2vtM3PfvjY2tjHG2JjwMLUB2wE3SjAkSC1EweEhQqMQSkrUqEJVIkWJokipqJL0'
        b'Q0UrNVRYpE0UJUKtQSkShfAoj0Bk7JhHYkMqk/Qag8HG9rWvfe/MvTPn7LX6Ye+ZO9cmVT50S6Nz5sze'
        b'e/5nrbX/67+WVFV0DQoOACLpxgFJT+j+2L12vjrguBuOk75JWiMACgiOID27icxuIT1XByanmvzkBz+k'
        b'0JAXCHOm9KztGac8FUmARDMwmfM6csr8U0H0DnOnMqdRRt559whFZ7K7E9slxqzF3El/mK84uOTn7mmN'
        b'J0uZSFopgojgDuKz4KS7YVpnBtEMM6jKisZUkyOHj/Luvv/hwP4xis57uDu7X3mdZtlGigLN4MzBJaEx'
        b'NxzD3DEHeu7dHUPSPYKLoKKoBIIqhSpBC1Q1e0dw0QzQKVttJsaPc/j4FEURKOhaDJrtkpY7ZcszmPxb'
        b'tmNyVUAwzCJ4BdEwwGIkulMauCiqAdWCUIAGoRBHpSIEJahmhxruQjSjihUmRrQK0WIWGBgEQSwg1nni'
        b'3dhxd9wSSLxEypJWq8nJyZNMTjeZmSkxE/r6hxgcHWVoqI9aUSFaQ8UwDQiKm2IoiHYN4m6YR5wKNKYX'
        b'6eLK8WAxggYwI5247KroWKyI5RRHx4+wfecOfvnarxg/NsFgnGRRbZoFAxWtWOdkWML8Zeez/opNrL/s'
        b'PAYHFkBtsBvQ7o549oILuCEecYvJzdIDzPN5EdUcoMleZvkTK7xqsXP3bh78t+/Tnj7Alo+V3HCNsW4t'
        b'LF4CRR9YBScOHuGl7a/z4ONP8fwLm7ju1i+ybvU5BK1QFFxxFEE6/kDEUQGR5OYuMDNIvJMtRYqdaMnv'
        b'lVc8/9IzPPnsv/KFG09y960lZ64AHQKKucd/8VLYcgl86rYmr77wLPc/9GsOv/d1Nn90A/PrdQoFcccl'
        b'9Bgln3wBRNEusBgREXoJU9xAjBlrs33Hzzj65vf4z38Y556vlSy+GHQ0gUISD8759IEuhI3Xw33fHueS'
        b'9j3seu5pJqYrSi+JGO42S9I5bDwD7QJz8w7ZZK4GxKgK55VdjzG5736+97fTnHcpxGGgljntg5k4BUYG'
        b'OLAS7v5qgz8e+Cde+eUTTLXAiDixQ5adCyKJbGeBdczYQS9Gmza7dj3JO7u38p2vTjO6DKQGHmGqCc2Z'
        b'zHO9fjTwSjhxRDkyJtjJ9Pq1hXDLl5qsmPhnXtu1g0asMjjLHOiICJZiqhdYcolLym5I5K2Db/Pi41v5'
        b'xlfaLLkIakOgLXhiW417v7mAe7+2mENjmsKyB9jB3c7W7wo7H5nPqz9exOTbNVAozoS7/qrB4Z33cuDg'
        b'IcoYc8iAuKAymx6VuXvm9OLMlC2eeeY/uPbK41x2haB1qAkceAte3b+I1ZtXsGR0mOFF9Tnu9AB9dfjo'
        b'p5awdN0Qcd4ZHHhjMNGRwrxVwu23NHj8R/fRaAnWOZneAeUg0mOx7GNDiBh7D+znyJvPceeXQOue+QV2'
        b'/Kqg79IlhGKEE5PTaOiEwGxcjS6GeYtL+hcMMXZskrffKmfnFMbm60vC4R3s+c3LmCsmYJLSG55O7BxX'
        b'Wr5px8irO1/gI5ubnLuSLihvwO8On8Wons2+MTg4PcG7jWqOjAHQYahPGL9+ZZLxsuKdxkwPcqid0eaT'
        b'1xq/eP5JyjZEqzC3pDo8gtBLsAmtmdGaabJ//2+5/RZHe51dgz+97H1qw89Su8pYtsUYWWinSSQZgNWb'
        b'xlm5UajiEI3jpyKH9Z8Q/v7RN2iePMHIvAI3xTMrzGF+PJ/GaDSnJqmaR1i96pQ/HIQrPtHuvvnvGyJQ'
        b'FFAUTp0pBodOn7NseaBqnKAxdYyR4UXgkkVkkk1zYgw33CrK1jR9tYqRkQ/491kt+AeN3zd9aKCGeot2'
        b'Y2JW34onWYT0nspESNFi0k/UUA+nKc3/lyHQKoVYOvVQoppypZDkVvReujDDPWX3UOujYJTj47GbIk4d'
        b'3WculO3A5ITSmFCsDH8QtmPHK0T66e/vR5SU3HNuM7xXKCaLCUJfrZ+R0bN447XXuGQNp/vCAVcOHRjh'
        b'0W2Rp16c4eB7KdcuWa5cd13Bp280zlhop53YzvqxN5yhkYUMjAyjIl2V3Kkj5qQkAVSFQgvOW30h2/9r'
        b'EIs95nGghGqyn8d/sIC7PzfJY080OH9Fjc9tqXPHTcK6CyseeqTi1ruMHTvrSW+dMsyEp58rueCiP2Jg'
        b'eB6EgARN+ZqEb86pFAEVKILyoYsu5LGXzuKd3+1j5fmGBKAN7RN9PLBVGBsb5xv3CJd+RAj16TnutSrw'
        b'1p5hHnhgimPvDfLJG5tZIKRx8mCNp7fXufsrH6dWH0CkwBRwwYze4E+FhmjirSIIC0cXcMGGTTz84xpt'
        b'g8ogNoWHtzmLlk7z3X+EDVc72mfdo9chYi0iKy8/yde/WfDiz2fYvac2izoKj/xUuXDNRi5aczGF1lEC'
        b'mqV2kmM6V/aoSOKgoAzUa2y48mPs2XM2b77ez/Q07B1zRhe3ueUO6J+fQTCXEjoFbSHOguUt7vzLwC/2'
        b'RipLyX58n/DvDw/xmVu/QK3oS1QhiTC0W8RkizlgWW+L5DgLBfOGR9j4J5/lX7bWmDg0wOiZcN2WJKE/'
        b'iJzkFJAq8KGL29x0ZaRoGV4GHto2wNqr/5ozly/FpdZVM6KCS4p07eWxBMy72R1VQujnnHMuYHDJp/mb'
        b'byt9VR0pTgf0fw0RWLgATJWfPd3P3sm/YMOVmxCpg2hSzdohWE3SR0IG5hBjTABTesdFcAIqdT58+VX0'
        b'j1zLl7+ljP33IF6lStuAyFw51vFAd1hg79463/rOPJ568c9Ze8X1BOlLFTtkOZ8bCiJIBtu1WDRLNJKF'
        b'tQPRwbxAwiAfv+YGlq/4M27+rPN39/RxdGwIb8scFF2FAuDCzMwgP31QufPLfRw8eRdrN95A0CLLm1Q8'
        b'4wkQmfk1h1O3vomx6tQFHemfyU5xL3D62XD5VZx91rk8+cRz3P+jl1m/doCNH46sWVOy/FxnaNRRh+OH'
        b'hZd31nn0oRaN9jpuvOOLLFuxkjJYqk8LcCkSqebA71hJRRHP6sLdiVXMzE9OqklnG2AoQoGLs2Tpedz+'
        b'+VXcMHETP39+Jw9u28PR9w8yNd3EUEIoGBk8g1XnrmbzNVdz/qb1oNByRy3tX2iBSgAEd8lSWmZ7X6IU'
        b'5BK9Kqtui8fNZk+XpzsTAa3hbmgIzF88j5tvW8XNn7mNqjVDozFFq12iRY2+kXnocJ22KTEabgYuhBw/'
        b'tRBAQvJQJxpyBycExYHC3bEYKcsS9yptgqVSyJMiF0+VnmNpQxRxo4qpcg8DgywYHkY1zWk7tKKj0SE6'
        b'5slNQaAIqfuTSuoESLNxkDQndCwWq0ir1SK2S2JVYRYxi7gbkiVvahtINykbdAPWLPfJJHdvPJV1YqCd'
        b'8BBQVYrQkVKdpkTqlblHLLVbCBIyMHNazWlmmk1aVYX5bGVsPlshC5IronzNALplsgugRE/NEk/sieXg'
        b'NoCiliTWbGZNLxQtNXRcUVcKr9pMTk1y+NB7NBvHqTogVHN3UDMR5tZRlidOAh3diZ46g+aSw1TnrBMN'
        b'qAYISmkGVYVK6JAS7hVVOUN7epKpRsSsTfHA/ffx7tEZ3j/wW6qyhbkjQVDpuCszsqag9O6fdaxhCYQH'
        b'wInmuGsWxLN9CfGOeZVIwF0xj0SLdOK8ape0p9scO3yI/wUvw+6ppw7nJgAAAABJRU5ErkJggg=='
    ),

}

import io
from typing import Dict, List, Tuple, Set, Any, Callable

RES_LIST = [
    'img/0.gif',
    'img/1.gif',
    'img/2.gif',
    'img/3.gif',
    'img/4.gif',
    'img/5.gif',
    'img/6.gif',
    'img/7.gif',
    'img/8.gif',
    'img/9.gif',
    'img/10.gif',
    'img/11.gif',
    'img/12.gif',
    'img/13.gif',
    'img/14.gif',
    'img/face1.gif',
    'img/face2.gif',
    'img/face3.gif',
]

RES_IOMAP: Dict[str, io.IOBase] = {}
RES_MISSING: List[Tuple[str, str]] = []

if 'RES_INLINE' in globals():
    RES_INLINE: Dict[str, bytes]
    # 资源已内联
    for res_path in RES_LIST:
        if res_path in RES_INLINE: # type: ignore
            RES_IOMAP[res_path] = io.BytesIO(RES_INLINE[res_path]) # type: ignore
        else:
            RES_MISSING.append((res_path, '内联资源不存在'))
else:
    # 资源未内联
    for res_path in RES_LIST:
        try:
            res_fp = open(res_path, 'rb')
            RES_IOMAP[res_path] = res_fp
        except BaseException as exc:
            RES_MISSING.append((res_path, str(exc)))

if RES_MISSING:
    import tkinter.messagebox as tkmsg
    missing_info = '加载以下资源失败：'
    for info in RES_MISSING:
        missing_info += '\n加载%s失败：%s' % info
    tkmsg.showerror(title='你说得对，但是',
                    message=missing_info)
    exit()
            

import tkinter as tk  # UI界面
import tkinter.messagebox as tkmsg
from PIL import Image, ImageTk
import random  # 随机数
import abc
import numpy as np, numpy.typing as npt
import math, fractions
import time, threading
from functools import partial


# 常量
BUTTON_STATES = {'E', 'M', 'B', 'X', 'F', 1, 2, 3, 4, 5, 6, 7, 8}
BUTTON_STATE_IMAGE_MAP = {
    0:   Image.open(fp=RES_IOMAP['img/0.gif']),   # 空白方块
    1:   Image.open(fp=RES_IOMAP['img/1.gif']),   # 数字1
    2:   Image.open(fp=RES_IOMAP['img/2.gif']),   # 数字2
    3:   Image.open(fp=RES_IOMAP['img/3.gif']),   # 数字3
    4:   Image.open(fp=RES_IOMAP['img/4.gif']),   # 数字4
    5:   Image.open(fp=RES_IOMAP['img/5.gif']),   # 数字5
    6:   Image.open(fp=RES_IOMAP['img/6.gif']),   # 数字6
    7:   Image.open(fp=RES_IOMAP['img/7.gif']),   # 数字7
    8:   Image.open(fp=RES_IOMAP['img/8.gif']),   # 数字8
    'B': Image.open(fp=RES_IOMAP['img/9.gif']),   # 爆炸雷
    'X': Image.open(fp=RES_IOMAP['img/10.gif']),  # 标错雷
    'F': Image.open(fp=RES_IOMAP['img/11.gif']),  # 旗子
    'E': Image.open(fp=RES_IOMAP['img/12.gif']),  # 立体方块
    'M': Image.open(fp=RES_IOMAP['img/13.gif']),  # 未爆炸雷
    'H': Image.open(fp=RES_IOMAP['img/14.gif']),  # 炸弹，作弊模式下使用
}
FACE_STATE_IMAGE_MAP = {
    'in_progress': Image.open(fp=RES_IOMAP['img/face1.gif']),  # 笑脸
    'success':     Image.open(fp=RES_IOMAP['img/face2.gif']),  # 耍酷脸
    'fail':        Image.open(fp=RES_IOMAP['img/face3.gif']),  # 哭脸
}

EASTER_EGG = False
if EASTER_EGG: print('EASTER_EGG = True，开启彩蛋')

def wrap_evt_handler(f: Callable[[], None]) -> Callable[[Any], None]:
    def evt_handler(evt: Any): f()
    return evt_handler


class MyPyMatrix: # 自定义二维数组类
    shape: Tuple[int, int]
    data: List[Any]

    # 注：初始化值应为不可变类型
    def __init__(self, shape: Tuple[int, int], init_val: Any) -> None:
        self.shape = shape
        n_rows, n_cols = shape
        self.data = [init_val] * (n_rows * n_cols)
    
    def get(self, x: int, y: int) -> Any:
        n_rows, n_cols = self.shape
        x_check = x >= 0 and x < n_cols
        y_check = y >= 0 and y < n_rows
        if x_check and y_check:
            return self.data[n_cols * y + x]
        else:
            raise IndexError
    
    # 如果索引越界，返回默认值
    def get_noerr(self, x: int, y: int, default: Any) -> Any:
        try:
            return self.get(x, y)
        except IndexError:
            return default
    
    def set(self, x: int, y: int, val: Any) -> None:
        n_rows, n_cols = self.shape
        x_check = x >= 0 and x < n_cols
        y_check = y >= 0 and y < n_rows
        if x_check and y_check:
            self.data[n_cols * y + x] = val
        else:
            raise IndexError
    
    # 如果索引越界，不做任何事
    def set_noerr(self, x: int, y: int, val: Any) -> None:
        try:
            self.set(x, y, val)
        except IndexError:
            pass
    
    def modify(self, x: int, y: int, modifier: Callable[[Any], Any]) -> None:
        n_rows, n_cols = self.shape
        x_check = x >= 0 and x < n_cols
        y_check = y >= 0 and y < n_rows
        if x_check and y_check:
            self.data[n_cols * y + x] = modifier(self.data[n_cols * y + x])
        else:
            raise IndexError
    
    # 如果索引越界，不做任何事
    def modify_noerr(self, x: int, y: int, modifier: Callable[[Any], Any]) -> None:
        try:
            self.modify(x, y, modifier)
        except IndexError:
            pass
    
    def copy(self):
        obj = MyPyMatrix(self.shape, None)
        obj.data = self.data.copy()
    
    def enumerate(self):
        n_rows, n_cols = self.shape
        for i, e in enumerate(self.data):
            yield (i % n_cols, i // n_cols), e


class MyTimer:
    begin_time: float
    thr_running: bool
    thr: threading.Thread
    tick_interval: float = 0.1
    on_tick: List[Callable[[float], None]]

    def __init__(self) -> None:
        self.on_tick = []
        self.reset()
        self.thr_running = True
        self.thr = threading.Thread(target=self._run, daemon=True)
        self.thr.start()

    def _run(self):
        # 虽然每次执行_tick的间隔是tick_interval
        # 但是由于这并不是RTOS，以及_tick和一系列回调执行本身需要时间
        # 所以tick_interval是最大误差，而不是计时单位
        while True:
            self._tick()
            time.sleep(self.tick_interval)

    def _tick(self):
        t = time.time()
        for f in self.on_tick: f(t - self.begin_time)

    def reset(self):
        self.begin_time = time.time()


class MineState:
    timer: MyTimer
    time_limit: int
    shape: Tuple[int, int] # 场地宽高
    hacked_view: bool # 是否作弊查看所有雷
    first_op_commited: bool # 是否已进行第一次操作
    n_mines: int # 地雷数
    n_success_left: int # 距离成功需要排除的空地数
    n_flags_left: int # 剩余可用标记数
    game_end: bool # 游戏是否结束
    success: bool # 游戏是否胜利
    mine_state_matrix: MyPyMatrix # 是否为雷
    revealed_state_matrix: MyPyMatrix # 是否已探索
    marked_state_matrix: MyPyMatrix # 是否标记
    surrounding_mines_matrix: MyPyMatrix # 周围雷数
    on_game_end: List[Callable[[bool], None]] # 游戏结束回调
    on_update: List[Callable[[Tuple[int, int]], None]] # 地块状态更新回调
    on_reset: List[Callable[[], None]] # 游戏数据重置回调
    on_param_change: List[Callable[[], None]] # 游戏参数重置回调
    on_time_change: List[Callable[[float], None]] # 时间更改回调

    def __init__(self,
        n_rows: int, n_cols: int,
        n_mines: int,
        time_limit: int,
    ) -> None:
        if EASTER_EGG:
            mine_ratio = fractions.Fraction(n_mines, n_rows * n_cols)
            print('数据：场地为%dx%d，共%d个雷，占%s' % (n_cols, n_rows, n_mines, str(mine_ratio)))
        self.time_limit = time_limit
        self.timer = MyTimer()
        self.timer.on_tick.append(self._on_tick)
        self.shape = (n_rows, n_cols)
        self.n_mines = n_mines
        self.on_game_end = []
        self.on_update = []
        self.on_reset = []
        self.on_param_change = []
        self.on_time_change = []
        self.reset_game()
    
    def reset_params(self,
        n_rows: int, n_cols: int,
        n_mines: int,
        time_limit: int,
    ) -> None:
        self.shape = (n_rows, n_cols)
        self.n_mines = n_mines
        self.time_limit = time_limit
        for f in self.on_param_change: f()
        self.reset_game()

    # 每0.1s（不准确）触发
    def _on_tick(self, t: float):
        if not self.first_op_commited:
            self.timer.reset()
        elif not self.game_end:
            # 如果时间限制为不是正数，那么不限时
            if self.time_limit > 0:
                if int(t) > self.time_limit: self._on_game_end(False)
            for f in self.on_time_change: f(t)

    # 只重置地雷数据
    def _reshuffle_mines(self, fix_data=None):
        self.mine_state_matrix = MyPyMatrix(self.shape, 0)
        self.surrounding_mines_matrix = MyPyMatrix(self.shape, 0)
        # 将地雷状态数组的前(地雷数量)个设为1，然后打乱
        if fix_data is None:
            for i in range(self.n_mines):
                self.mine_state_matrix.data[i] = 1
            random.shuffle(self.mine_state_matrix.data)
        else:
            self.mine_state_matrix.data = fix_data
        for (x, y), state in self.mine_state_matrix.enumerate():                
            if state:
                inc = lambda x: x + 1
                # 更新周围雷数
                self.surrounding_mines_matrix.modify_noerr(x - 1, y - 1, inc)
                self.surrounding_mines_matrix.modify_noerr(x - 1, y, inc)
                self.surrounding_mines_matrix.modify_noerr(x - 1, y + 1, inc)
                self.surrounding_mines_matrix.modify_noerr(x, y - 1, inc)
                self.surrounding_mines_matrix.modify_noerr(x, y, inc)
                self.surrounding_mines_matrix.modify_noerr(x, y + 1, inc)
                self.surrounding_mines_matrix.modify_noerr(x + 1, y - 1, inc)
                self.surrounding_mines_matrix.modify_noerr(x + 1, y, inc)
                self.surrounding_mines_matrix.modify_noerr(x + 1, y + 1, inc)

    # 重置游戏数据
    def reset_game(self):
        self.first_op_commited = False
        self.hacked_view = False
        n_rows, n_cols = self.shape
        self.game_end = False
        self.success = False
        self.n_success_left = n_rows * n_cols - self.n_mines
        self.n_flags_left = self.n_mines
        self.revealed_state_matrix = MyPyMatrix(self.shape, False)
        self.marked_state_matrix = MyPyMatrix(self.shape, False)
        self._reshuffle_mines()
        for f in self.on_reset: f()

    # 探索某位置
    def reveal(self, pos: Tuple[int, int]):
        if self.game_end: return
        # 如果标记过，探索无效
        if self.marked_state_matrix.get(*pos): return
        # 如果该位置已探索，探索无效
        if self.revealed_state_matrix.get(*pos): return
        # 如果首次探索，保证探索点不是雷且触发扩展探索
        if not self.first_op_commited:
            self.first_op_commited = True
            n_auto_remake = 0
            while self.mine_state_matrix.get(*pos) \
               or self.surrounding_mines_matrix.get(*pos) != 0:
                self._reshuffle_mines()
                n_auto_remake += 1
            if EASTER_EGG:
                print('你知道吗？系统为你自动重开了%d次，每次开局都是一种幸运。'
                      % n_auto_remake)
        
        # 探索主流程
        self.revealed_state_matrix.set(*pos, True)
        for f in self.on_update: f(pos)
        if self.mine_state_matrix.get(*pos):
            self._on_game_end(False)
        else:
            self.n_success_left -= 1
            if self.surrounding_mines_matrix.get(*pos) == 0:
                # 空格，扩展探索
                explored = set([pos])
                for npos in self._get_surrounding_pos(pos):
                    self._reveal_expand(npos, explored)
            if self.n_success_left <= 0: # 正常情况下不可能小于0，兜个底
                self._on_game_end(True)
    
    def _get_surrounding_pos(self, pos: Tuple[int, int]):
        x, y = pos; n_rows, n_cols = self.shape
        for ny in range(max(y-1, 0), min(y+1+1, n_rows)):
            for nx in range(max(x-1, 0), min(x+1+1, n_cols)):
                if not (ny == y and nx == x): yield (nx, ny)
    
    # 扩展探索直到遇到周围雷数不为0或有雷的格
    def _reveal_expand(self, pos: Tuple[int, int], explored: Set[Tuple[int, int]]):
        if pos in explored: return
        explored.add(pos)
        if self.mine_state_matrix.get(*pos): return
        # 如果未标记且未探索，记为已探索
        if not self.marked_state_matrix.get(*pos) and \
           not self.revealed_state_matrix.get(*pos):
            self.revealed_state_matrix.set(*pos, True)
            for f in self.on_update: f(pos)
            self.n_success_left -= 1
        if self.surrounding_mines_matrix.get(*pos) != 0: return
        for npos in self._get_surrounding_pos(pos):
            self._reveal_expand(npos, explored)

    # 标记某位置
    def mark(self, pos: Tuple[int, int]):
        if self.game_end: return
        # 如果该位置已探索，标记无效
        if self.revealed_state_matrix.get(*pos): return
        
        # 标记主流程
        if self.marked_state_matrix.get(*pos):
            # 取消标记
            self.n_flags_left += 1
        else:
            # 标记
            # 如果没有多余的标记限额，标记无效
            if self.n_flags_left == 0: return
            self.n_flags_left -= 1
        self.marked_state_matrix.modify(*pos, lambda x: not x)
        for f in self.on_update: f(pos)
    
    # 作弊，如果是雷则标记，不是则探索
    def hack_alright(self, pos: Tuple[int, int]):
        if self.marked_state_matrix.get(*pos):
            self.mark(pos) # 取消标记
        if self.mine_state_matrix.get(*pos) and self.first_op_commited:
            self.mark(pos)
        else:
            self.reveal(pos)
    
    # 作弊，显示所有雷
    def hack_viewall(self):
        if not self.first_op_commited: return
        self.hacked_view = not self.hacked_view
        for pos, is_mine in self.mine_state_matrix.enumerate():
            if is_mine:
                for f in self.on_update: f(pos)
    
    # 作弊，自动通关
    def hack_complete(self):
        self.hack_alright(self.get_rand_pos())
        for pos, is_mine in self.mine_state_matrix.enumerate():
            self.hack_alright(pos)

    # 游戏结束时触发
    def _on_game_end(self, success: bool):
        self.game_end = True
        self.success = success
        for f in self.on_game_end: f(success)
    
    # 强制结束游戏
    def force_end(self, success: bool):
        self._on_game_end(success)
    
    def get_rand_pos(self):
        n_rows, n_cols = self.shape
        rx = random.randint(0, n_cols-1)
        ry = random.randint(0, n_rows-1)
        return (rx, ry)


class ButtonField:
    tk_frame: tk.Frame
    game_state: MineState
    buttons_matrix: MyPyMatrix # 按钮
    button_size: int
    button_state_image_map: Dict[Any, ImageTk.PhotoImage]

    @property
    def tk_obj(self): return self.tk_frame

    def __init__(self,
        master,
        game_state: MineState,
        button_size: int
    ) -> None:
        self.button_state_image_map = {k: ImageTk.PhotoImage(v.resize((button_size, button_size)))
                                       for k, v in BUTTON_STATE_IMAGE_MAP.items()}
        self.game_state = game_state
        self.game_state.on_update.append(self._on_update)
        self.game_state.on_game_end.append(self._on_game_end)
        self.game_state.on_reset.append(self._reset_buttons)
        self.game_state.on_param_change.append(self._on_reset_params)
        
        self.button_size = button_size
        self.tk_frame = tk.Frame(master=master)
        self.tk_frame.pack_propagate(False)
        self._init_buttons()
        self._reset_buttons()

    def _init_buttons(self): # 初始化按钮
        n_rows, n_cols = self.game_state.shape
        self.tk_frame.configure(width=n_cols*self.button_size, height=n_rows*self.button_size)
        self.buttons_matrix = MyPyMatrix(self.game_state.shape, None)
        for y in range(n_rows):
            for x in range(n_cols):
                btn = tk.Button(master=self.tk_frame)
                btn.bind(sequence="<Button-1>", func=wrap_evt_handler(partial(self.game_state.reveal, (x, y))))
                btn.bind(sequence="<Button-2>", func=wrap_evt_handler(partial(self.game_state.hack_alright, (x, y))))
                btn.bind(sequence="<Button-3>", func=wrap_evt_handler(partial(self.game_state.mark, (x, y))))
                btn.place(
                    width=self.button_size, height=self.button_size,
                    x=(x*self.button_size), y=(y*self.button_size)
                )
                self.buttons_matrix.set(x, y, btn)
    
    def _on_reset_params(self): # 重置UI状态
        btn: tk.Button
        for btn in self.buttons_matrix.data:
            btn.destroy()
        self.buttons_matrix.data.clear()
        self._init_buttons()
    
    def _reset_buttons(self): # 重置按钮状态
        btn: tk.Button
        for btn in self.buttons_matrix.data:
            btn.config(image=self.button_state_image_map['E'])

    # 某位置状态更新时触发
    def _on_update(self, button_pos: Tuple[int, int]):
        x, y = button_pos
        self.buttons_matrix.get(x, y).config(
            image=self.button_state_image_map[self._decide_button_state(x, y)]
        )
    
    # 游戏结束时触发
    def _on_game_end(self, success: bool):
        for (x, y), revealed in self.game_state.revealed_state_matrix.enumerate():
            if not revealed:
                self.buttons_matrix.get(x, y).config(
                    image=self.button_state_image_map[self._decide_final_state(x, y)]
                )

    # 决定按钮如何显示
    def _decide_button_state(self, x: int, y: int):
        if not self.game_state.revealed_state_matrix.get(x, y): # 未探索
            if self.game_state.hacked_view and self.game_state.mine_state_matrix.get(x, y):
                return 'H'
            elif self.game_state.marked_state_matrix.get(x, y): # 已标记
                return 'F'
            else: # 未标记
                return 'E'
        else: # 已探索
            if self.game_state.mine_state_matrix.get(x, y): # 是雷
                return 'B'
            else: # 不是雷
                return self.game_state.surrounding_mines_matrix.get(x, y)
    
    # 决定游戏结束后未探索的按钮如何显示
    def _decide_final_state(self, x: int, y: int):
        if self.game_state.mine_state_matrix.get(x, y): # 是雷
            return 'M'
        else: # 不是雷
            if self.game_state.marked_state_matrix.get(x, y): # 已标记
                return 'X'
            else: # 未标记
                return 'E'


class StatusHeader:
    tk_frame: tk.Frame
    game_state: MineState
    face_btn: tk.Button
    n_flags_label: tk.Label
    time_used_label: tk.Label
    face_button_size: int
    field_button_size: int
    face_state_image_map: Dict[Any, ImageTk.PhotoImage]

    @property
    def tk_obj(self): return self.tk_frame

    def __init__(self,
        master,
        game_state: MineState,
        face_button_size: int,
        field_button_size: int
    ) -> None:
        self.face_state_image_map = {k: ImageTk.PhotoImage(v.resize((face_button_size, face_button_size)))
                                     for k, v in FACE_STATE_IMAGE_MAP.items()}
        self.game_state = game_state
        self.game_state.on_update.append(self._on_update)
        self.game_state.on_game_end.append(self._on_game_end)
        self.game_state.on_reset.append(self._reset_ui)
        self.game_state.on_param_change.append(self._set_width)
        self.game_state.on_time_change.append(self._on_time_change)
        
        self.face_button_size = face_button_size
        self.field_button_size = field_button_size
        self.tk_frame = tk.Frame(master=master, bg='white', relief="sunken")
        self.face_btn = tk.Button(self.tk_frame, relief='raised')
        self.face_btn.bind(sequence="<Button-1>", func=wrap_evt_handler(self.game_state.reset_game))
        self.face_btn.bind(sequence="<Button-2>", func=wrap_evt_handler(self.game_state.hack_complete))
        self.face_btn.bind(sequence="<Button-3>", func=wrap_evt_handler(self.game_state.hack_viewall))
        self.n_flags_label = tk.Label(self.tk_frame, bg='white', fg='red', font=('幼圆', 22))
        self.time_used_label = tk.Label(self.tk_frame, bg='white', fg='red', font=('幼圆', 22))
        
        self.tk_frame.pack_propagate(False)
        self._set_width()
        self._reset_ui()
    
    def _reset_ui(self):
        self.face_btn.config(image=self.face_state_image_map['in_progress'])
        self.n_flags_label.config(text=str(self.game_state.n_flags_left))
        self.time_used_label.config(text='0')
    
    def _set_width(self):
        width = max(self.field_button_size * self.game_state.shape[1], 9 * self.face_button_size)
        self.tk_frame.config(width=width, height=self.face_button_size)
        self.face_btn.place(relx=0.5, rely=0.5, anchor='center',
                            width=self.face_button_size, height=self.face_button_size)
        self.n_flags_label.place(relx=0.0, rely=0.5, x=self.face_button_size, anchor='center',
                                 width=self.face_button_size*2, height=self.face_button_size)
        self.time_used_label.place(relx=1.0, rely=0.5, x=-self.face_button_size*2, anchor='center',
                                   width=self.face_button_size*4, height=self.face_button_size)

    # 某位置状态更新时触发
    def _on_update(self, button_pos: Tuple[int, int]):
        self.n_flags_label.config(text=str(self.game_state.n_flags_left))
    
    # 游戏结束时触发
    def _on_game_end(self, success: bool):
        status = 'success' if success else 'fail'
        self.face_btn.config(image=self.face_state_image_map[status])
    
    # 游戏进行中每0.1s（不准确）触发
    def _on_time_change(self, t: float):
        if self.game_state.time_limit <= 0:
            self.time_used_label.config(text='%d' % int(t))
        else:
            self.time_used_label.config(text='%d/%d' % (int(t), self.game_state.time_limit))
    

class ParamPanel:
    tk_frame: tk.Frame
    time_limit_checkbox_bvar: tk.BooleanVar
    auto_sweeper_hack_checkbox_bvar: tk.BooleanVar
    game_state: MineState
    automata: 'AutoMineSweeper'

    @property
    def tk_obj(self): return self.tk_frame

    def __init__(self, master, game_state: MineState) -> None:
        self.game_state = game_state
        self.automata = EqSolverSweeper(self.game_state)

        # 由pygubu根据可视化设计生成
        self.tk_frame = tk.Frame(master)
        self.n_rows_label = tk.Label(self.tk_frame)
        self.n_rows_label.configure(text="行数")
        self.n_rows_label.grid(column=0, columnspan=2, row=0)
        self.n_rows_input = tk.Entry(self.tk_frame)
        self.n_rows_input.grid(column=2, row=0)
        self.n_cols_label = tk.Label(self.tk_frame)
        self.n_cols_label.configure(text="列数")
        self.n_cols_label.grid(column=0, columnspan=2, row=1)
        self.n_cols_input = tk.Entry(self.tk_frame)
        self.n_cols_input.grid(column=2, row=1)
        self.n_mines_label = tk.Label(self.tk_frame)
        self.n_mines_label.configure(text="地雷数")
        self.n_mines_label.grid(column=0, columnspan=2, row=2)
        self.n_mines_input = tk.Entry(self.tk_frame)
        self.n_mines_input.grid(column=2, row=2)
        self.time_limit_label = tk.Label(self.tk_frame)
        self.time_limit_label.configure(text="时间限制")
        self.time_limit_label.grid(column=0, row=3)
        self.time_limit_checkbox_bvar = tk.BooleanVar()
        self.time_limit_checkbox = tk.Checkbutton(self.tk_frame,
                                   variable=self.time_limit_checkbox_bvar,
                                   command=self._set_time_limit_input_state)
        self.time_limit_checkbox.grid(column=1, row=3)
        self.time_limit_input = tk.Entry(self.tk_frame)
        self.time_limit_input.grid(column=2, row=3)
        self.reminder_label = tk.Label(self.tk_frame)
        self.reminder_label.configure(text='\n'.join([
            "时间限制<=0表示不限时",
            "重置UI延迟较高，保存更改后请耐心等待",
        ]))
        self.reminder_label.grid(column=0, columnspan=3, row=4)
        self.submit_button = tk.Button(self.tk_frame,
                                       command=self.dump_data)
        self.submit_button.configure(text="保存更改并重置游戏")
        self.submit_button.grid(column=0, columnspan=3, row=5)
        self.hack_hint_label = tk.Label(self.tk_frame)
        self.hack_hint_label.configure(text='\n'.join([
            "关于作弊：",
            "雷是完全随机打乱的，所以死局很正常",
            "对某地块点中键，做出必然正确的选择",
            "对笑脸按钮点中键直接通关",
            "对笑脸按钮点右键显示所有雷的位置",
        ]))
        self.hack_hint_label.grid(column=0, columnspan=3, row=6)
        self.auto_sweeper_frame = tk.Frame(self.tk_frame)
        self.auto_sweeper_frame.configure(height=200, width=200)
        self.auto_sweeper_button = tk.Button(self.auto_sweeper_frame,
                                             command=self.automata)
        self.auto_sweeper_button.configure(text="自动扫雷")
        self.auto_sweeper_button.pack(side="left")
        self.auto_sweeper_hack_checkbox_bvar = tk.BooleanVar()
        self.auto_sweeper_hack_checkbox = tk.Checkbutton(self.auto_sweeper_frame,
                                          variable=self.auto_sweeper_hack_checkbox_bvar,
                                          command=self._set_automata_hack)
        self.auto_sweeper_hack_checkbox.configure(text="不失败")
        self.auto_sweeper_hack_checkbox.pack(side="top")
        self.auto_sweeper_frame.grid(column=0, columnspan=3, row=7)
        self.tk_frame.grid_anchor("center")
        self.load_data()
    
    def _set_automata_hack(self):
        self.automata.use_hack = self.auto_sweeper_hack_checkbox_bvar.get()
    
    def _set_time_limit_input_state(self):
        use_time_limit = self.time_limit_checkbox_bvar.get()
        self.time_limit_input.config(state=('normal' if use_time_limit else 'disabled'))
    
    def dump_data(self):
        try:
            n_rows = int(self.n_rows_input.get())
            n_cols = int(self.n_cols_input.get())
            n_mines = int(self.n_mines_input.get())
            use_time_limit = self.time_limit_checkbox_bvar.get()
            time_limit_str = self.time_limit_input.get()
            time_limit = int(time_limit_str) if use_time_limit else 0
            self.game_state.reset_params(n_rows, n_cols, n_mines, time_limit)
        except:
            tkmsg.showerror(title='你说得对，但是',
                            message='输入值转换错误，请检查您的输入')
    
    def load_data(self):
        n_rows, n_cols = self.game_state.shape
        self.n_rows_input.delete(0, "end")
        self.n_rows_input.insert(0, str(n_rows))
        self.n_cols_input.delete(0, "end")
        self.n_cols_input.insert(0, str(n_cols))
        self.n_mines_input.delete(0, "end")
        self.n_mines_input.insert(0, str(self.game_state.n_mines))
        if self.game_state.time_limit <= 0:
            self.time_limit_checkbox_bvar.set(False)
            self.time_limit_input.delete(0, "end")
            self.time_limit_input.insert(0, str(0))
        else:
            self.time_limit_checkbox_bvar.set(True)
            self.time_limit_input.delete(0, "end")
            self.time_limit_input.insert(0, str(self.game_state.time_limit))


class MineSweeperUI:
    tk_frame: tk.Frame
    subframe_left: tk.Frame
    game_state: MineState
    status_header: StatusHeader
    button_field: ButtonField
    param_panel: ParamPanel

    @property
    def tk_obj(self): return self.tk_frame
    
    def __init__(self,
        master,
        n_rows: int, n_cols: int,
        n_mines: int,
        time_limit: int,
        field_button_size: int,
        face_button_size: int,
    ) -> None:
        self.game_state = MineState(n_rows, n_cols, n_mines, time_limit)
        self.tk_frame = tk.Frame(master=master)
        self.subframe_left = tk.Frame(master=self.tk_frame)
        self.status_header = StatusHeader(self.subframe_left, self.game_state,
                                          face_button_size, field_button_size)
        self.status_header.tk_obj.pack(side='top')
        self.button_field = ButtonField(self.subframe_left, self.game_state, field_button_size)
        self.button_field.tk_obj.pack(side='top')
        self.param_panel = ParamPanel(self.tk_frame, self.game_state)
        self.subframe_left.pack(side='left')
        self.param_panel.tk_obj.pack(side='left')


class MainWin:
    FIELD_BUTTON_SIZE = 20 # 扫雷场地按钮大小
    FACE_BUTTON_SIZE = 40 # 笑脸按钮大小

    def __init__(self,
        n_rows: int, n_cols: int,
        n_mines: int,
        time_limit: int,
    ) -> None:
        self.root = tk.Tk()
        self.root.title('扫雷')
        self.ui = MineSweeperUI(self.root, n_rows, n_cols, n_mines, time_limit,
                                self.FIELD_BUTTON_SIZE, self.FACE_BUTTON_SIZE)
        self.ui.tk_obj.pack()
        self.root.resizable(width=False, height=False)


# 冷知识：扫雷是NP-Complete问题
class AutoMineSweeper(abc.ABC):
    game: MineState
    use_hack: bool
    thr: threading.Thread

    def __init__(self, game: MineState, use_hack: bool = False) -> None:
        self.game = game
        self.use_hack = use_hack
        self.thr = threading.Thread(target=self.run)
    
    def reveal(self, pos: Tuple[int, int]):
        if self.use_hack:
            self.game.hack_alright(pos)
        else:
            self.game.reveal(pos)
    
    @abc.abstractmethod
    def run(self): pass
    
    def __call__(self):
        if self.game.game_end: return
        if not self.thr.is_alive():
            if self.thr.ident is not None:
                self.thr = threading.Thread(target=self.run)
            self.thr.start()


class BogoSweeper(AutoMineSweeper):
    '''
    完全随机地探索地块直到游戏结束
    这个Bogo是猴子排序(Bogo Sort)的那个Bogo
    '''
    def run(self):
        while not self.game.game_end:
            self.reveal(self.game.get_rand_pos())


class EqSolverSweeper(AutoMineSweeper):
    '''
    将扫雷场地的一部分当做方程求解
    时间复杂度很高，也不能保证一定赢(事实上几乎赢不了)
    而且有时候还会卡死
    '''
    # 暴力尝试不定方程的所有01解，O(2^n)
    def solve_bruteforce(self, unknown_coeff_mat: npt.NDArray, n_mines: npt.NDArray):
        results: List[int] = []
        n_rows, n_cols = unknown_coeff_mat.shape
        for bitmask in range(2 ** n_cols):
            bitmask_left = bitmask
            result = np.zeros_like(n_mines); col = 0
            while bitmask_left:
                if bitmask_left & 1: result += unknown_coeff_mat[:, col]
                col += 1; bitmask_left >>= 1
            if np.array_equal(result, n_mines): results.append(bitmask)
        return results
    
    def is_known_point(self, pos: Tuple[int, int]):
        return self.game.revealed_state_matrix.get(*pos) \
           and self.game.surrounding_mines_matrix.get(*pos)

    # 随机得已探索且周围雷数不为0的起始点
    def get_start_point(self):
        valid_pos = False
        while not (valid_pos):
            start_point = self.game.get_rand_pos()
            valid_pos = self.is_known_point(start_point)
        return start_point # type: ignore
    
    # 选择随机已知点周围的已知点建立方程
    def collect_unknown(self):
        knowns = False
        while not knowns:
            pos = self.get_start_point()
            knowns = {p for p in self.game._get_surrounding_pos(pos)
                      if self.is_known_point(p)}
        knowns.add(pos) # type: ignore
        unknowns = {}
        for kpos in knowns:
            for spos in self.game._get_surrounding_pos(kpos):
                if not self.game.revealed_state_matrix.get(*spos):
                    unknowns[spos] = 0
        for i, k in enumerate(unknowns):
            unknowns[k] = i
        unknown_coeff_mat = np.zeros((len(knowns), len(unknowns)), np.uint8)
        n_mines = np.ndarray((len(knowns),), np.uint8)
        for i, kpos in enumerate(knowns):
            n_mines[i] = self.game.surrounding_mines_matrix.get(*kpos)
            for spos in self.game._get_surrounding_pos(kpos):
                if not self.game.revealed_state_matrix.get(*spos):
                    unknown_coeff_mat[i, unknowns[spos]] = 1
        return unknown_coeff_mat, n_mines, unknowns

    def run(self):
        get_bit = lambda x, n: (x >> n) & 1
        if not self.game.first_op_commited:
            self.reveal(self.game.get_rand_pos())
        while not self.game.game_end:
            unknown_coeff_mat, n_mines, unknowns = self.collect_unknown()
            results = self.solve_bruteforce(unknown_coeff_mat, n_mines)
            chosen = random.choice(results)
            for pos, i in unknowns.items():
                if not get_bit(chosen, i):
                    self.reveal(pos)


if __name__ == '__main__':
    main = MainWin(20, 20, 96, 2 * 60)
    main.root.mainloop()
