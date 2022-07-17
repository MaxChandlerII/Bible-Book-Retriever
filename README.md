# Bible-Book-Retriever
This project will retrieve a book of the Bible, in the translation you desire, from the internet, then store locally in a word document. If desired, it can parse out the verses.

# Committing 
- Using Git Bash
   * Using Git Bash, set user.name and user.email to your profile
   * In Git Bash push commits up (git push origin main)
   * Git Bash prompted me for credentials, opted for signing-in online (not the token option), authorized a Git Credential Manager, was prompted to enter password, was authorized (technically my Device was authorized)
      * Token option was not approved

- Set user.name and user.email per Repo
   * https://www.git-tower.com/learn/git/faq/change-author-name-email

# Python Links/Libraries/Functions
https://stackabuse.com/reading-and-writing-ms-word-files-in-python-via-python-docx-module/
- Runs: 
   * A run in a word document is a continuous sequence of words having similar properties, such as similar font sizes, font shapes, and font styles.
   * Can use Runs once I've set the highlight color of words in the Word Doc. Highlighted words will be a Run and non-highlighted Runs will be another Run.
   * Highlighting using Runs
      * https://www.geeksforgeeks.org/working-with-highlighted-text-in-python-docx-module/

- Headers
   * Info on creating Headers. Could be useful for setting each Chapter # as a Header, to provide an Outline to easily navigate the document with.

# FEATURE IDEAS
- Removing Verse #'s
	* when trying to determine the verses to remove, you know it starts at 1. You can set something up to index through the entire chapter and to search for the next subsuquent #, which should greatly improve the odds of removing ONLY verse #'s instead of accidentially removing #'s that aren't verses. 
	* This isn't 100% error proof, perhaps an extremely sophisticated method would use an AI library or would simply have to read the words preceeding a # to see if it gives indication that it's about to mention a # and if it does, then leave it be and perhaps make note of it for the user to say "hey we detected in this sentence that it was about to mention a # so we didn't remove this (insert #) # from the text."
	
- Removing Chapter Headings
	* perhaps the easiest way for this would be to look at the html for the text in the website and see if it differs from the "body" of the text and if it does and IF the user wants the chapter headings removed then go ahead and delete them. 
	Or if they want to keep them perhaps have a table that stores the location of the header (like after these 3x words and before these 3x words) and then i know the location of the header and could paste it in with unique spacing before/after to help differentiate it from the "body" of the text
	
- Legal
	* May need to post a legal disclaimer that any Bible translation has its own legal disclaimer and terms of use that the user is responsible for knowing and following and that this tool is in no way responsible for the user's use of that copy righted material.
	* My tool itself may actually face restrictions in copy/pasting Bible translations for others to use? Perhaps when I paste any Bible translation I need to also paste that translation's legal disclaimer?
	
- Word/Phrase Highlighting
	* May be venturing too far into a full-fledged tool like Logos or a tool like a Concordance. But, perhaps I offer a feature where the user can type a word or phrase and then the tool underlines/italicizes/bolds/sets font color/highlights that word/phrase all throughout the text they've requested? 
	* Furthermore, perhaps I also provide a list of verses in which that word/phrase appears?
	
- Ease of Use
	* In order to make it simple for others to use, I think it the final product should be an executable (.exe) that others can download.
	
- Compatability
	* Should others want to use it on a Mac or Linux machine, that will require some thinking on how to get a copmuter/VM? with one of those OS'es to work on.
	* Not everyone may have Microsoft Word. 
		* May want to add a feature to securely connect to one's Google Docs?
		* Are there mark-up/down languages tools that could be leveraged?
