# Problem 2: Planning App
#
# You are designing an app for your festival to help attendees have the best experience possible!
# As part of the application, users will be able to easily search their favorite artist and find
# out the day, time, and stage the artist is playing at. Write a function get_artist_info() that
# accepts a string artist and a dictionary festival_schedule mapping artist's names to dictionaries
# containing the day, time, and stage they are playing on. Return the dictionary containing the
# information about the given artist.
#
# If the artist searched for does not exist in festival_schedule, return the dictionary {"message": "Artist not found"}.
#
## If the artist searched for does not exist in festival_schedule, return the dictionary {"message": "Artist not found"}.


from typing import Dict


def get_artist_info(artist: str, festival_schedule: Dict) -> Dict:
    result = festival_schedule.get(artist)
    if result is None:
        return {"message": "Artist not found"}
    return result


festival_schedule = {
    "Blood Orange": {"day": "Friday", "time": "9:00 PM", "stage": "Main Stage"},
    "Metallica": {"day": "Saturday", "time": "8:00 PM", "stage": "Main Stage"},
    "Kali Uchis": {"day": "Sunday", "time": "7:00 PM", "stage": "Second Stage"},
    "Lawrence": {"day": "Friday", "time": "6:00 PM", "stage": "Main Stage"},
}

print(get_artist_info("Blood Orange", festival_schedule))
print(get_artist_info("Taylor Swift", festival_schedule))
print(get_artist_info("", festival_schedule))
