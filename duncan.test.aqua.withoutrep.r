#/bin/bash/Rscript
args=commandArgs(T)

origindata <- read.table(args[1],header = TRUE, sep = "\t")
#origindata <- read.table("six.txt",header = TRUE, sep = "\t")
datnames <- names(origindata)

library(agricolae)
library(ggplot2)
#length(names)

pdf(args[2])
for (i in 2:length(datnames)){
    fit <- aov(origindata[, i] ~ origindata[, 1])
    result <- duncan.test(fit, "origindata[, 1]", alpha = 0.05)
    datmeans <- result$means
    datgroups <- result$groups
    print(datgroups)
    ind <- match(row.names(datmeans), row.names(datgroups))
    datmeans$groups <- datgroups$groups[ind]
    names(datmeans)[1] <- datnames[i]
    plotdata <- as.data.frame(cbind(row.names(datmeans), datmeans[, 1], datmeans$std, as.character(datmeans$groups)))
    names(plotdata) <- c("Treat", "y", "std", "groups")
    plotdata$y <- as.numeric(as.character(plotdata$y))
    plotdata$std <- as.numeric(as.character(plotdata$std))
    #barplot(plotdata$y)
    #pdf(paste("plot",i,".pdf",sep = ""))
    theplot <- ggplot(data = plotdata, mapping = aes(x = Treat, y = y, fill = Treat)) + geom_bar(stat = 'identity')  + labs(title = datnames[i], x = "Samples", y= datnames[i]) + geom_errorbar(aes(ymin = y - std, ymax = y + std), width = 0.2, position=position_dodge(0.9)) + ylim(min(0,min(plotdata$y)-max(plotdata$std)), max(max(plotdata$y)+max(plotdata$std), max(plotdata$y) * 1.2)) + geom_text(mapping = aes(y = y + std, label = groups), vjust = -1)
    print(theplot)
    #dev.off()
}
dev.off()
