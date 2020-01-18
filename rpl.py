'''Script to initialize a reddit bot to make spotify playlists from reddit threads
	based on user suggestions, ie "What are the best songs of the 2010's?", 
	"What are the essential 90's Pump up songs"
Abbreviations:
E := There exists
PL:= Playlist
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
                     password= pw,
                     user_agent='Spotify playlist bot by /u/SamAndre')

#listing the subreddit the script will run on
subreddit = reddit.subreddit("AskReddit")

#Keyword for executing the script
keyphrase = "!song"

#Initialize Spotipy
spotify = spotipy.Spotify()
#TODO

#Starting to analyze the comments
for comment in subreddit.stream.comments():
		if keyphrase in comment.body:
				''' Check to see if there is already a playlist 
				for this thred, create one if necessary, then go into 
				adding the songs.
				Need to see how to differentiate between the parent ID being a 
				submittion_id or a comment'''
				#check to see if E PL for this thread
				if comment.parent() is Submission: #Checks to see if we are at a top level comment
 					results = spotify.search(q = comment.parent().title, type = "playlist")
 					
					try:
						#Now begin to check parent for song and look it up
						txt = comment.parent()
						#from the parent comment check to see if its a song
						'''
						process the text to see if it can be a song. 
						Problems:
						- If the comment contains more than just the song and artist
						I will need to try and find the song.
						-What if the song I add isn't correct
						(will need to add a second command and edit the playlist)
						-if there are multiple songs that are similar titles/remakes
						how can i differentiate'''
					except:
						reddit.comment("Sorry, your song was not found on spotify")