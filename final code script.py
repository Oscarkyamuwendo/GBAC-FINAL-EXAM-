            #STEP 1: Install ZSH SHELL

		sudo apt-get update
		sudo apt-get install zsh
	
            #After installation, you can start Zsh by typing zsh and pressing Enter.
            #Once Zsh is installed, you may want to customize it further using frameworks like Oh My Zsh or Prezto.
       
	
          #STEP 2. Install command: (this l did by running the command below on my terminal)
	        #For Mac
	brew install zsh-autosuggestions

          #STEP 3. Activating the auto suggestions
          #To activate the autosuggestions,l added the following at the end of your .zshrc
	        #to open .zshrc type vim .zshrc in your terminal

  source $(brew --prefix)/share/zsh-autosuggestions/zsh-autosuggestions.zsh

        #STEP 4. Final step
        #At last l closed the terminal and opened it again then next was magic happening on my termminal where l got suggestipns of commands which had written before and this helped me to save time l would spend on typing 


        #I used VIM as a tool to help me edit text in my blog and save it locally on my machine several times using 
        the terminal and then push it once on github 

	 "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

        #Once Homebrew is installed, you can install Vim with the following command:


	brew install vim
        #After the installation is complete, you can run Vim by typing vim in the Terminal.



        #UPDATING OF CONTENT IN THE LOCAL REPOSITORY TO THE REPOSITORY ON GITHUB**

      #STEP 1 ( How l created a public key)

	ssh-keygen -t rsa -b 4096 -C "your_email@example.com"


	      #To display the content of your public key, you can use the following command:**
	
	cat ~/.ssh/id_rsa.pub

        #Copy the output and use it wherever you need to add your public key.

	
	git clone git@github.com:username/repository.git
 
        #Open your terminal and navigate to the local directory of the cloned Git repository.

	cd /path/to/cloned/repository
	     

        #Check the Status:
        #It's a good practice to check the status of your local repository to see which files have been modified, added, or deleted.


	git status
	
        #Add and Commit Changes:
git add .
git commit -m "Your commit message here"
	

        #Finally, push your changes to the GitHub repository. If you cloned the repository using HTTPS, you might be prompted to enter your GitHub credentials.

	git push origin master
         #Then you are able to find your content on git hub
	 







 


