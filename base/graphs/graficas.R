#! /usr/local/bin/Rscript --vanilla

statistics <- read.csv("statistics.csv", header = TRUE)

#GRAFICAS STATISTICS
png("graph_statistics.png", width=1024, units="px")
plot(statistics$precision, type="b", ylim=c(0,1),
     axes=T, ann=T, xlab="Threshold", ylab="", cex.lab=0.8, lwd=1.2, pch=17)
box()
lines(statistics$recall, type="b", lty=2, lwd=2, pch=18)
lines(statistics$fmeasure, type="b", lty=3, lwd=2, pch=19)
lines(statistics$accuracy, type="b", lty=4, lwd=2, pch=25)
lines(statistics$goodnes, type="b", lty=5, lwd=2, pch=21)
legend("bottomleft", names(statistics[c(-1,-2,-3,-4,-5)]), cex=1.3, 
   lty=1:5, lwd=2, pch=c(17,18,19,25,21), bty="nb")
title(main="Relevance of results (for many threshold values)")
garbage <- dev.off()

#STATISTICS WITH ZOOM
png("graph_statistics_zoom.png", width=1024, units="px")
plot(statistics$precision, type="b", ylim=c(0.4,1),
     axes=T, ann=T, xlab="Threshold", ylab="", cex.lab=0.8, lwd=1.2, pch=17,
     xlim=c(5,20))
box()
lines(statistics$recall, type="b", lty=2, lwd=2, pch=18)
lines(statistics$fmeasure, type="b", lty=3, lwd=2, pch=19)
lines(statistics$accuracy, type="b", lty=4, lwd=2, pch=25)
lines(statistics$goodnes, type="b", lty=5, lwd=2, pch=21)
legend("bottomleft", names(statistics[c(-1,-2,-3,-4,-5)]), cex=1.3, 
   lty=1:5, lwd=2, pch=c(17,18,19,25,21), bty="nb")
title(main="Relevance of results (for many threshold values)")
garbage <- dev.off()

#GRAFICAS TP, FN, TN, FP
png("graph_tp_fn.png", width=1024, units="px")
barplot(t(statistics[c(2,3)]), main="Title", ylab="Title Y", xlab="Threshold",
          ylim=c(0,40),space=0.3, cex.axis=0.8, las=1, cex=0.8,
          names.arg=statistics$threshold, legend=rownames(t(statistics[c(2,3)]))) 
garbage <- dev.off()

png("graph_tn_fp.png", width=1024, units="px")
barplot(t(statistics[c(4,5)]), main="Title", ylab="Title Y", xlab="Threshold",
          ylim=c(0,60),space=0.3, cex.axis=0.8, las=1, cex=0.8,
          names.arg=statistics$threshold, legend=rownames(t(statistics[c(4,5)]))) 
garbage <- dev.off()

#NORMALIZADAS
ntp <- function(x) {x/37}
ntn <- function(x) {x/55}
normed <- statistics
normed$tp <- lapply(normed$tp, ntp)
normed$fn <- lapply(normed$fn, ntp)
normed$tn <- lapply(normed$tn, ntn)
normed$fp <- lapply(normed$fp, ntn)

png("graph_tp_fn_norm.png", width=1024, units="px")
barplot(t(normed[c(2,3)]), main="Title", ylab="Title Y", xlab="Threshold",
          ylim=c(0,1),space=0.3, cex.axis=0.8, las=1, cex=0.8,
          names.arg=statistics$threshold, legend=rownames(t(statistics[c(2,3)]))) 
garbage <- dev.off()

png("graph_tn_fp_norm.png", width=1024, units="px")
barplot(t(normed[c(4,5)]), main="Title", ylab="Title Y", xlab="Threshold",
          ylim=c(0,1),space=0.3, cex.axis=0.8, las=1, cex=0.8,
          names.arg=statistics$threshold, legend=rownames(t(statistics[c(4,5)]))) 
garbage <- dev.off()


#COMPENSACION FN Y FP
png("comp_fn_fp.png", width=1024, units="px")
compensed <- statistics$fn - statistics$fp
barplot(compensed, main="Compensacion FN y FP", xlab="Threshold",
        names.arg=statistics$threshold, ylim=c(-60,60), space=0.3)
garbage <- dev.off()