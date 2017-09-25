
library(wordcloud2)
library(data.table)
library(stringr)

currentloc <- dirname(parent.frame(2)$ofile)
setwd(currentloc)

# get data ---------------------------
dataFile <- 'monta_data.csv'

data <- read.csv(dataFile, sep=";", fileEncoding="", encoding="UTF-8")

colnames(data)<- c("id","created_at","name","tweettext","rtcount","favcount","twurl")

dt = data.table(data)
texts <- dt$tweettext
texts <-as.character(texts)
Encoding(texts)<-"UTF-8"

lump = paste(unlist(texts), collapse =" ")
lump2<-lump
words = strsplit(lump2, " ")


wordstoremove <- c("rt","#MontaÄäntä", "RT","@SiniHelminen" ,"ja","\n","","#klassikkotwiitti","#montaääntä")

(words <- as.data.frame(sapply(words, function(x) 
  gsub(paste(wordstoremove, collapse = '|'), '', x))))

#-----------------------------------
# counts the frequencies of words
words.freq <- table(words)


ss <- data.frame(x=unlist( words ))
sss <- setDT(ss)[, .(freq = .N), x]

sss <- sss[order(sss$freq, decreasing = TRUE)]
osio <- sss[1:100,]


# ------------------------------------
# do the wordcloud

wordcloud2(data = osio, size=5)

#letterCloud(data=osio, word = "o", size=3)

# ---------------------
