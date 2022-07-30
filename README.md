# Bible-Book-Retriever
This project will retrieve a book of the Bible, in the translation you desire, from the internet, then store locally in a word document. If desired, it can parse out the verses.

# Committing 
## Using Git Bash
   * Using Git Bash, set user.name and user.email to your profile
   * In Git Bash push commits up (git push origin main)
   * Git Bash prompted me for credentials, opted for signing-in online (not the token option), authorized a Git Credential Manager, was prompted to enter password, was authorized (technically my Device was authorized)
      * Token option was not approved

## Set user.name and user.email per Repo
   * https://www.git-tower.com/learn/git/faq/change-author-name-email
   * git config user.name ______
   * git config user.email ___ncsu___

## Checking credentials entered
	* git config --list --show-origin
	* https://www.geeksforgeeks.org/how-to-set-git-username-and-password-in-gitbash/


# Python Links/Libraries/Functions
https://stackabuse.com/reading-and-writing-ms-word-files-in-python-via-python-docx-module/
## Runs: 
   * A run in a word document is a continuous sequence of words having similar properties, such as similar font sizes, font shapes, and font styles.
   * Can use Runs once I've set the highlight color of words in the Word Doc. Highlighted words will be a Run and non-highlighted Runs will be another Run.
   * Highlighting using Runs
      * https://www.geeksforgeeks.org/working-with-highlighted-text-in-python-docx-module/

## Headers
   * Info on creating Headers. Could be useful for setting each Chapter # as a Header, to provide an Outline to easily navigate the document with.


# FEATURE IDEAS
## Removing Verse #'s
	* when trying to determine the verses to remove, you know it starts at 1. You can set something up to index through the entire chapter and to search for the next subsuquent #, which should greatly improve the odds of removing ONLY verse #'s instead of accidentially removing #'s that aren't verses. 
	* This isn't 100% error proof, perhaps an extremely sophisticated method would use an AI library or would simply have to read the words preceeding a # to see if it gives indication that it's about to mention a # and if it does, then leave it be and perhaps make note of it for the user to say "hey we detected in this sentence that it was about to mention a # so we didn't remove this (insert #) # from the text."
	
## Removing Chapter Headings
	* perhaps the easiest way for this would be to look at the html for the text in the website and see if it differs from the "body" of the text and if it does and IF the user wants the chapter headings removed then go ahead and delete them. 
	Or if they want to keep them perhaps have a table that stores the location of the header (like after these 3x words and before these 3x words) and then i know the location of the header and could paste it in with unique spacing before/after to help differentiate it from the "body" of the text

## Word/Phrase Highlighting
	* May be venturing too far into a full-fledged tool like Logos or a tool like a Concordance. But, perhaps I offer a feature where the user can type a word or phrase and then the tool underlines/italicizes/bolds/sets font color/highlights that word/phrase all throughout the text they've requested? 
	* Furthermore, perhaps I also provide a list of verses in which that word/phrase appears?

## Ease of Use
	* In order to make it simple for others to use, I think it the final product should be an executable (.exe) that others can download.
	
## Compatability
	* Should others want to use it on a Mac or Linux machine, that will require some thinking on how to get a copmuter/VM? with one of those OS'es to work on.
	* Not everyone may have Microsoft Word. 
		* May want to add a feature to securely connect to one's Google Docs?
		* Are there mark-up/down languages tools that could be leveraged?
	

# Legal
- May need to post a legal disclaimer that any Bible translation has its own legal disclaimer and terms of use that the user is responsible for knowing and following and that this tool is in no way responsible for the user's use of that copy righted material.
- My tool itself may actually face restrictions in copy/pasting Bible translations for others to use? Perhaps when I paste any Bible translation I need to also paste that translation's legal disclaimer?

# Removing Sensitive Data from Git Repo (ex: credentials, passwords, etc.)
1. View Git's suggestions 
	* https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/removing-sensitive-data-from-a-repository
2. Using the BFG method:
	* Download BFG via their website:
		- https://rtyley.github.io/bfg-repo-cleaner/
	* Create a new (empty) folder anywhere that is NOT in a Git repo already
	* In the new folder run the following Git command to clone a **mirror** of your ENTIRE Git repo
	* Git clone --mirror git://example.com/some-big-repo.git
	* Now in your "new" folder you'll have a folder with your entire Git repo
	* Copy/paste the BFG jar file you downloaded earlier into this "new" folder at the same level as your ENTIRE git repo folder
	* Run the following Git cmd
	* bfg --delete-files file_name_you_want_deleted  your-repo-name.git
	* You'll see some info appear on your terminal about the cleaning BFG just did. View the report which will be in a folder at the same level as your Git repo
	* Run the following Git cmd
	* cd your-repo-name.git
	* Run the following Git cmd
	* git reflog expire --expire=now --all && git gc --prune=now --aggressive
	* Run the following Git cmd
	* git push
	* Now your Remote repo will be updated with the cleaning even though you'll still see those commits in your history, the commits will be empty.
	
# Setting Up Google Project / API
1. Google - Google Docs API, Python Quick Start. Used for knowing libraries to install, creating Google Project, and creating Credentials
	* https://developers.google.com/docs/api/quickstart/python
2. Set up Google Project
	* https://developers.google.com/workspace/guides/create-project
3. Enable Google Drive API & Enable Google Docs API
	* https://developers.google.com/workspace/guides/enable-apis
4. pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib
5. pip install --upgrade httplib2
6. Reference this helpful blog
	* https://towardsdatascience.com/how-to-load-the-content-of-a-google-document-in-python-1d23fd8d8e52
7. Create an OAuth 2.0 Client ID
	* https://developers.google.com/workspace/guides/create-credentials#desktop-app (see OAuth, used "Desktop Application")
8. Download the OAuth Client in .json format, save as "credentials.json". Place in same folder as the .py file(s).
9. Use Google's code to extract text from a Google Doc (don't forget to update w/your Doc's "Document ID")
	* https://developers.google.com/docs/api/samples/extract-text#python
10. NEXT STEP: Pick up with this link on extracting text from Google Doc, saving to a .txt file and then using it.
	* https://towardsdatascience.com/how-to-load-the-content-of-a-google-document-in-python-1d23fd8d8e52