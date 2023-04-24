# The text from the cover letter
text = "Dear Mrs Müller, I am writing to express my interest in joining Food Robots Inc. as a Food Processing Automation Engineer. I came across the job posting on Monster.com, and I believe my background in food processing and my experience with light-based communication technology make me an ideal candidate for this position. Your company's pioneering work in manufacturing robots for the food production industry is impressive. I was particularly intrigued by the recent research paper you published, exploring alternatives to conventional communication methods like cables and Wi-Fi for robots in food production environments. This resonates with a project I completed during my time at the University of Applied Sciences, where I developed a light-based communication solution called the LiFi Project. The LiFi Project leverages visible light communication to transmit data between devices, providing a fast, secure, and wireless solution ideal for sensitive environments like food production facilities. This technology offers several advantages over traditional Wi-Fi, such as higher data transfer rates, reduced electromagnetic interference, and greater security. I am confident that my hands-on experience with the LiFi Project could be highly beneficial for Food Robots Inc.'s ongoing research efforts. In addition to my experience with the LiFi Project, my academic background in sustainable packaging solutions and my internships in the food processing industry have equipped me with the necessary skills to excel in this role. I am eager to contribute to your team and help Food Robots Inc. advance its mission to revolutionize the food production industry with innovative robotic solutions. Thank you for considering my application. I am excited about the opportunity to contribute to Food Robots Inc. and would appreciate the chance to further discuss my qualifications and how they align with your needs. Please feel free to contact me at 0541 1234 567 or greta.algoritz@hs-osnabrueck.de to schedule a conversation. Sincerely, Greta Algoritz"

# A list of words
word_list = text.split(" ")

# Print the first 50 entries
print(word_list[0:49])

# The length of the list
word_list_length = len(word_list)
print(f"The length of the list is: {word_list_length}")

# Convert all to lowercase
word_list_lower = []
for word in word_list:
    word_list_lower.append(word.lower())

# Print the first 50 entries
print(word_list_lower[0:49])


# Check for given keywords
keywords = ["lifi", "digitalization", "python"]

for k in keywords:
    if k in word_list_lower:
        print(f"The word {k} is mentioned in the cover letter.")
    else:
        print(f"The word {k} is not mentioned in the cover letter.")

# Another list with unique words
unique_words_list = []
for word in word_list_lower:
    if word not in unique_words_list:
        unique_words_list.append(word)

print(f"There are { len(unique_words_list) } in the cover letter. Compared to { len(word_list_lower) } total words.")
