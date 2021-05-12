## Assassin's Creed Odyssey: Project Review

* Site publication: <https://amw6765.github.io/AssassinsCreedPROJECT/>
* GitHub: <https://github.com/amw6765/AssassinsCreedPROJECT/>
* Developers: Anthony Wlodarczyk, Isaac Esterline, Danny Hough, Josh Sige
* Date of Evaluation: 2021-05-11
* Evaluated by: @ebeshero

### Project introduction and research questions
Your first three pages (moving from left to right on your navigation bar) provide a helpful orientation to *Assassin's Creed*, the *Odyssey* game and its characters and your project research. The description of your project could use a little refinement to clarify what *kinds* of information you wanted to visualize in your "distant reading" text analysis, facilitated by computers. That is often best written *last* in a project, after you've set up your visualizations and analysis in place. 

The Characters page helps to orient us to the sheer number of characters we'll meet in the game. It leaves us with some questions, though:
* How are these characters organized? Is it by first time they appear in the script? I don’t think it’s alphabetical order.   
* It would be nice to see the characters in the script be linked, maybe to their first speaking role , or to some data about how often each one speaks in the script. Which characters appear most frequently in the game?
* Is the Kassandra storyline potentially available for possible expansion of this project?


### Website design and user experience
The site is well coordinated with its topic. The Romanesque block capitals make it seem a bit like a classical monument (more Roman than Greek), but fit your content. For legibility I'd recommend backing off from capitalizing *all* the body text: the capitals work best in your headings. 

There's an accessibility problem on the site landing page (index.html): Taking a picture of text removes that text from searching on the web. It definitely makes an impression, but it is not accessible to those who aren’t able to read images (people using screen readers, blind readers, colorblind readers who have trouble with depth perception.) But you can still overlay text on an image in HTML: A better method if you want to put an image behind text is to use it as a background on a div or section. You can even set this in CSS! Here's some good example code of a background image set in a `<div>` element:
<https://www.freecodecamp.org/news/how-to-add-an-image-url-to-your-div/> This way, you still get the cool effect of text over image, but you can still highlight that text with your mouse and make it searchable or readable in the code view of your stie. 

On the Process page you did the reverse and made a super accessible page with your code samples full blocked in the HTML. Nice work on the Code page of blocking your code using `<pre>` elements to preserve the formatting! That makes it easier for coders learning from your work to work with in future!

You should correct a typo on Creators page: “semseter” => “semester”

## Visualizations and analysis

The visual.html page features some intricate SVG graphs! Your write-ups could use a bit more detail to help orient us not just to what we're seeing, but *how* you derived the information. So, for the SVG graph showing actions to speakers in a chapter: You should define what you mean by “actions” in the context of this game script: do you mean action as in gameplay? It is impressive to see which portions of the game have the most dialogue!

It might be interesting to combine your two SVGs to get Speeches, Actions, and Speakers at once. Yes, I know that would be a challenge to plot but I think you could do it with thinner bars to fit across the screen. We could then quickly see at a glance which chapters have the most dialogue AND the most actions (like “The Road to the Symposium”. 

The explanation of the Top Ten Peoples and Places could use a little refinement: You say, “This information shows the lack of diversity of different peoples and places in Greece that existed in the same timeframe.” Doesn’t that assume that this game is a *direct representation of actual history*? (Are you sure if that’s the case?) Maybe it would be more accurate to say that this suggests a lack of diverse Mediterranean cultures represented in this game. (Why do these results seem limited——did you expect to see more cultural diversity represented?) 

On the NLP graphs, you should also explain what the numbers on the Y axis mean: these are actual counts of each term associated with peoples and cultures: how often these appear in the game, right? HOW MANY entities were output from the named entity program, and how often was each mentioned in the game? You also might comment more on the context in which these entities are referenced—for some of the most and least popular. How are Spartans usually referred to? Why do you think “Greek” is referenced so few times (under 10?)

The interactive network is a fascinating way to interact with that dense data cloud on characters! But you should explain the meaning of the colors making the connections. What is green, and red, and blue? How were connections made? Was it based on co-occuring in the same chapter? 

Because this network is so dense, it *is* a little offputting without a little more help to navigate it. A next step would be to take some of the more interesting historic figures, and/or the highest degree characters (the ones with the most connections OTHER than Alexios) and create **sub-networks** from them to see who they’re connected to. We could look at  a subnetwork just for Sophokles or Euripedes, right? We could also make a subnetwork just representing only the red connections. (And another for the blue, and a third for the green) to supplement what you have here and help us to see a little better some of the connections we can expect to find in each portion of the game.

On the Process page, you might want to explain what’s going on in that complex set of if statements in the Python Spacy graph: this helps us understand your process and what you decided to filter out of your infographics. We could also really use a view of your XML markup to help understand the context for your XQuery script. 

## Concluding remarks
You pulled together to produce an appealing study of characters, game actions, and cultural representation in *Assassin's Creed Odyssey*. The analysis could use more detailed explanation to help viewers who are unfamiliar with how you structured your analysis (how you modeled the markup, how you "pulled" your data for those fascinating visuals). The project has "strong bones," by which I mean, you created a well structured foundation for your markup (your document data model), and that means you had a good understanding of what you could analyze and visualize. Overall, this is a very good team accomplishment and fine finish to the semester! 


