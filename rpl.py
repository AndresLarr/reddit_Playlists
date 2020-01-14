'''Script to initialize a reddit bot to make spotify playlists from reddit threads
	based on user suggestions, ie "What are the best songs of the 2010's?", 
	"What are the essential 90's Pump up songs"
'''

#Imports
import praw #reddit api wrapper
import spotipy #spotify wrapper
import request


#Password input to avoid leaking accounts password
pw = input("Please input password")


reddit = praw.Reddit(client_id='snho9d7xZNlVjA',
                     client_secret='Mv_fK5H2hkAiTNvVAj7YQjr4BM8',
                     username='PlaylistsBot',
                     password='nCLXgM2N.RZkKhg',
                     user_agent='Spotify playlist bot by /u/SamAndre')