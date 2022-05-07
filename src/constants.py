from colr import color

version = "1.255"
enablePrivateLogging = False
hide_names = False



sockets = {
    "skin": "bcef87d6-209b-46c6-8b19-fbe40bd95abc",
    "skin_level": "e7c63390-eda7-46e0-bb7a-a6abdacd2433",
    "skin_chroma": "3ad1b2b2-acdb-4524-852f-954a76ddae0a",
    "skin_buddy": "77258665-71d1-4623-bc72-44db9bd5b3b3",
    "skin_buddy_level": "dd3bf334-87f3-40bd-b043-682a57a8dc3a"
}



AGENTCOLORLIST = {
            "neon": (28, 69, 161),
            "none": (100, 100, 100),
            "viper": (48, 186, 135),
            "yoru": (52, 76, 207),
            "astra": (113, 42, 232),
            "breach": (217, 122, 46),
            "brimstone": (217, 122, 46),
            "cypher": (245, 240, 230),
            "jett": (154,222,255),
            "kay/o": (133, 146, 156),
            "killjoy": (255, 217, 31),
            "omen": (71, 80, 143),
            "phoenix": (254, 130, 102),
            "raze": (217, 122, 46),
            "reyna": (181, 101, 181),
            "sage": (90, 230, 213),
            "skye": (192, 230, 158),
            "sova": (37, 143, 204),
            "chamber": (200, 200, 200),
            "fade": (92, 92, 94)
        }


GAMEPODS = {
    "aresriot.aws-rclusterprod-mes1-1.eu-gp-bahrain-awsedge-1": "Bahrain",
    "aresriot.aws-rclusterprod-mes1-1.ext1-gp-bahrain-awsedge-1": "Bahrain",
    "aresriot.aws-rclusterprod-mes1-1.tournament-gp-bahrain-awsedge-1": "Bahrain",
    "aresriot.aws-rclusterprod-bog1-1.latam-gp-bogota-1": "Bogota",
    "aresriot.aws-rclusterprod-usw2-1.tournament-gp-cmob-1": "CMOB 1",
    "aresriot.aws-rclusterprod-usw2-1.tournament-gp-cmob-2": "CMOB 2",
    "aresriot.aws-rclusterprod-usw2-1.tournament-gp-cmob-3": "CMOB 3",
    "aresriot.aws-rclusterprod-usw2-1.tournament-gp-cmob-4": "CMOB 4",
    "aresriot.mtl-riot-ord2-3.latam-gp-chicago-1": "Chicago",
    "aresqa.aws-rclusterprod-dfw1-1.dev1-gp-dallas-1": "Dallas",
    "aresqa.aws-rclusterprod-usw2-3.dev1-gp-tournament-2": "Esports New",
    "aresqa.aws-rclusterprod-usw2-3.dev1-gp-tournament-1": "Esports Old",
    "aresqa.aws-rclusterprod-euc1-1.dev1-gp-frankfurt-1": "Frankfurt",
    "aresqa.aws-rclusterprod-euc1-1.stage1-gp-frankfurt-1": "Frankfurt",
    "aresriot.aws-rclusterprod-euc1-1.ext1-gp-eu1": "Frankfurt",
    "aresriot.aws-rclusterprod-euc1-1.tournament-gp-frankfurt-1": "Frankfurt",
    "aresriot.aws-rclusterprod-euc1-1.eu-gp-frankfurt-1": "Frankfurt 1",
    "aresriot.aws-rclusterprod-euc1-1.eu-gp-frankfurt-awsedge-1": "Frankfurt 2",
    "aresriot.aws-rclusterprod-ape1-1.ext1-gp-hongkong-1": "Hong Kong",
    "aresriot.aws-rclusterprod-ape1-1.tournament-gp-hongkong-1": "Hong Kong",
    "aresriot.aws-rclusterprod-ape1-1.ap-gp-hongkong-1": "Hong Kong 1",
    "aresriot.aws-rclusterprod-ape1-1.ap-gp-hongkong-awsedge-1": "Hong Kong 2",
    "aresriot.mtl-riot-ist1-2.eu-gp-istanbul-1": "Istanbul",
    "aresriot.mtl-riot-ist1-2.tournament-gp-istanbul-1": "Istanbul",
    "aresriot.aws-rclusterprod-euw2-1.eu-gp-london-awsedge-1": "London",
    "aresriot.aws-rclusterprod-euw2-1.tournament-gp-london-awsedge-1": "London",
    "aresriot.aws-rclusterprod-mad1-1.eu-gp-madrid-1": "Madrid",
    "aresriot.aws-rclusterprod-mad1-1.tournament-gp-madrid-1": "Madrid",
    "aresriot.mtl-tmx-mex1-1.ext1-gp-mexicocity-1": "Mexico City",
    "aresriot.mtl-tmx-mex1-1.latam-gp-mexicocity-1": "Mexico City",
    "aresriot.mtl-tmx-mex1-1.tournament-gp-mexicocity-1": "Mexico City",
    "aresriot.mia1.latam-gp-miami-1": "Miami",
    "aresriot.mia1.tournament-gp-miami-1": "Miami",
    "aresriot.aws-rclusterprod-aps1-1.ap-gp-mumbai-awsedge-1": "Mumbai",
    "aresriot.aws-rclusterprod-aps1-1.tournament-gp-mumbai-awsedge-1": "Mumbai",
    "aresriot.aws-rclusterprod-usw2-1.tournament-gp-offline-1": "Offline 1",
    "aresriot.aws-rclusterprod-usw2-1.tournament-gp-offline-2": "Offline 2",
    "aresriot.aws-rclusterprod-usw2-1.tournament-gp-offline-3": "Offline 3",
    "aresriot.aws-rclusterprod-usw2-1.tournament-gp-offline-4": "Offline 4",
    "aresriot.aws-rclusterprod-usw2-1.tournament-gp-offline-5": "Offline 5",
    "aresriot.aws-rclusterprod-usw2-1.tournament-gp-offline-6": "Offline 6",
    "aresriot.aws-rclusterprod-usw2-1.tournament-gp-offline-7": "Offline 7",
    "aresriot.aws-rclusterprod-usw2-1.tournament-gp-offline-8": "Offline 8",
    "aresriot.aws-rclusterprod-euw3-1.tournament-gp-paris-1": "Paris",
    "aresriot.aws-rclusterprod-euw3-1.eu-gp-paris-1": "Paris 1",
    "aresriot.aws-rclusterprod-euw3-1.eu-gp-paris-awsedge-1": "Paris 2",
    "aresriot.mtl-ctl-scl2-2.ext1-gp-santiago-1": "Santiago",
    "aresriot.mtl-ctl-scl2-2.latam-gp-santiago-1": "Santiago",
    "aresriot.mtl-ctl-scl2-2.tournament-gp-santiago-1": "Santiago",
    "aresriot.aws-rclusterprod-sae1-1.ext1-gp-saopaulo-1": "Sao Paulo",
    "aresriot.aws-rclusterprod-sae1-1.tournament-gp-saopaulo-1": "Sao Paulo",
    "aresriot.aws-rclusterprod-sae1-1.br-gp-saopaulo-1": "Sao Paulo 1",
    "aresriot.aws-rclusterprod-sae1-1.br-gp-saopaulo-awsedge-1": "Sao Paulo 2",
    "aresriot.aws-rclusterprod-apne2-1.ext1-gp-seoul-1": "Seoul",
    "aresriot.aws-rclusterprod-apne2-1.tournament-gp-seoul-1": "Seoul",
    "aresriot.aws-rclusterprod-apne2-1.kr-gp-seoul-1": "Seoul 1",
    "aresriot.aws-rclusterprod-apne2-1.kr-gp-seoul-awsedge-1": "Seoul 2",
    "aresriot.aws-rclusterprod-apse1-1.ext1-gp-singapore-1": "Singapore",
    "aresriot.aws-rclusterprod-apse1-1.tournament-gp-singapore-1": "Singapore",
    "aresriot.aws-rclusterprod-apse1-1.ap-gp-singapore-1": "Singapore 1",
    "aresriot.aws-rclusterprod-apse1-1.ap-gp-singapore-awsedge-1": "Singapore 2",
    "aresriot.aws-rclusterprod-eun1-1.tournament-gp-stockholm-1": "Stockholm",
    "aresriot.aws-rclusterprod-eun1-1.eu-gp-stockholm-1": "Stockholm 1",
    "aresriot.aws-rclusterprod-eun1-1.eu-gp-stockholm-awsedge-1": "Stockholm 2",
    "aresriot.aws-rclusterprod-apse2-1.ext1-gp-sydney-1": "Sydney",
    "aresriot.aws-rclusterprod-apse2-1.tournament-gp-sydney-1": "Sydney",
    "aresriot.aws-rclusterprod-apse2-1.ap-gp-sydney-1": "Sydney 1",
    "aresriot.aws-rclusterprod-apse2-1.ap-gp-sydney-awsedge-1": "Sydney 2",
    "aresriot.aws-rclusterprod-apne1-1.eu-gp-tokyo-1": "Tokyo",
    "aresriot.aws-rclusterprod-apne1-1.ext1-gp-kr1": "Tokyo",
    "aresriot.aws-rclusterprod-apne1-1.tournament-gp-tokyo-1": "Tokyo",
    "aresriot.aws-rclusterprod-apne1-1.ap-gp-tokyo-1": "Tokyo 1",
    "aresriot.aws-rclusterprod-apne1-1.ap-gp-tokyo-awsedge-1": "Tokyo 2",
    "aresriot.aws-rclusterprod-atl1-1.na-gp-atlanta-1": "US Central (Georgia)",
    "aresriot.aws-rclusterprod-atl1-1.tournament-gp-atlanta-1": "US Central (Georgia)",
    "aresriot.mtl-riot-ord2-3.na-gp-chicago-1": "US Central (Illinois)",
    "aresriot.mtl-riot-ord2-3.tournament-gp-chicago-1": "US Central (Illinois)",
    "aresriot.aws-rclusterprod-dfw1-1.na-gp-dallas-1": "US Central (Texas)",
    "aresriot.aws-rclusterprod-dfw1-1.tournament-gp-dallas-1": "US Central (Texas)",
    "aresriot.aws-rclusterprod-use1-1.na-gp-ashburn-1": "US East (N. Virginia 1)",
    "aresriot.aws-rclusterprod-use1-1.na-gp-ashburn-awsedge-1": "US East (N. Virginia 2)",
    "aresriot.aws-rclusterprod-use1-1.ext1-gp-ashburn-1": "US East (N. Virginia)",
    "aresriot.aws-rclusterprod-use1-1.pbe-gp-ashburn-1": "US East (N. Virginia)",
    "aresriot.aws-rclusterprod-use1-1.tournament-gp-ashburn-1": "US East (N. Virginia)",
    "aresriot.aws-rclusterprod-usw1-1.na-gp-norcal-1": "US West (N. California 1)",
    "aresriot.aws-rclusterprod-usw1-1.na-gp-norcal-awsedge-1": "US West (N. California 2)",
    "aresriot.aws-rclusterprod-usw1-1.ext1-gp-na2": "US West (N. California)",
    "aresriot.aws-rclusterprod-usw1-1.pbe-gp-norcal-1": "US West (N. California)",
    "aresriot.aws-rclusterprod-usw1-1.tournament-gp-norcal-1": "US West (N. California)",
    "aresriot.aws-rclusterprod-usw2-1.na-gp-oregon-1": "US West (Oregon 1)",
    "aresriot.aws-rclusterprod-usw2-1.na-gp-oregon-awsedge-1": "US West (Oregon 2)",
    "aresriot.aws-rclusterprod-usw2-1.pbe-gp-oregon-1": "US West (Oregon)",
    "aresriot.aws-rclusterprod-usw2-1.tournament-gp-oregon-1": "US West (Oregon)",
    "aresqa.aws-rclusterprod-usw2-3.dev1-gp-1": "US West 1",
    "aresqa.aws-rclusterprod-usw2-3.stage1-gp-1": "US West 1",
    "aresqa.aws-rclusterprod-usw2-3.dev1-gp-4": "US West 2",
    "aresriot.aws-rclusterprod-waw1-1.eu-gp-warsaw-1": "Warsaw",
    "aresriot.aws-rclusterprod-waw1-1.tournament-gp-warsaw-1": "Warsaw"
}


symbol = "■"
PARTYICONLIST = [
            color(symbol, fore=(227, 67, 67)),
            color(symbol, fore=(216, 67, 227)),
            color(symbol, fore=(67, 70, 227)),
            color(symbol, fore=(67, 227, 208)),
            color(symbol, fore=(94, 227, 67)),
            color(symbol, fore=(226, 237, 57)),
            color(symbol, fore=(212, 82, 207)),
            symbol
        ]


NUMBERTORANKS = [
            color('Unrated', fore=(46, 46, 46)),
            color('Unrated', fore=(46, 46, 46)),
            color('Unrated', fore=(46, 46, 46)),
            color('Iron 1', fore=(72, 69, 62)),
            color('Iron 2', fore=(72, 69, 62)),
            color('Iron 3', fore=(72, 69, 62)),
            color('Bronze 1', fore=(187, 143, 90)),
            color('Bronze 2', fore=(187, 143, 90)),
            color('Bronze 3', fore=(187, 143, 90)),
            color('Silver 1', fore=(174, 178, 178)),
            color('Silver 2', fore=(174, 178, 178)),
            color('Silver 3', fore=(174, 178, 178)),
            color('Gold 1', fore=(197, 186, 63)),
            color('Gold 2', fore=(197, 186, 63)),
            color('Gold 3', fore=(197, 186, 63)),
            color('Platinum 1', fore=(24, 167, 185)),
            color('Platinum 2', fore=(24, 167, 185)),
            color('Platinum 3', fore=(24, 167, 185)),
            color('Diamond 1', fore=(216, 100, 199)),
            color('Diamond 2', fore=(216, 100, 199)),
            color('Diamond 3', fore=(216, 100, 199)),
            color('Immortal 1', fore=(221, 68, 68)),
            color('Immortal 2', fore=(221, 68, 68)),
            color('Immortal 3', fore=(221, 68, 68)),
            color('Radiant', fore=(255, 253, 205)),
        ]

tierDict = {
            "0cebb8be-46d7-c12a-d306-e9907bfc5a25": (0, 149, 135),
            "e046854e-406c-37f4-6607-19a9ba8426fc": (241, 184, 45),
            "60bca009-4182-7998-dee7-b8a2558dc369": (209, 84, 141),
            "12683d76-48d7-84a3-4e09-6985794f0445": (90, 159, 226),
            "411e4a55-4e59-7757-41f0-86a53f101bb5": (239, 235, 101),
            None: None
        }
