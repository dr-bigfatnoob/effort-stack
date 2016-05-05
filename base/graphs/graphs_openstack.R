#! /usr/local/bin/Rscript --vanilla

commits <- read.csv("output_commits.csv", header = FALSE)

col <- ncol(commits)-12
added_commits <- colSums(commits[,1:col])

#added_commits

png("graph_commits.png", width=1024, units="px")
plot(added_commits, type="l", ylab="Commits per month", xlab="Months project life")
garbage <- dev.off()
