#/bin/bash/Rscript
args=commandArgs(T)
library(agricolae)
library(ggplot2)
#length(names)

pdf("plots.pdf")

firstdata <- read.table(args[1],header = TRUE, sep = "\t")
#origindata <- read.table("six.txt",header = TRUE, sep = "\t")
datnames <- names(firstdata)

for (i in 2:length(datnames)){
    allplotdata <- NULL
    for (n in 1:length(args)) {
        origindata <- read.table(args[n],header = TRUE, sep = "\t")
        fit <- aov(origindata[, i] ~ origindata[, 1])
        result <- duncan.test(fit, "origindata[, 1]", alpha = 0.05)
        datmeans <- result$means
        datgroups <- result$groups
        print(datnames[i])
        print(datgroups)
        ind <- match(row.names(datmeans), row.names(datgroups))
        datmeans$groups <- datgroups$groups[ind]
        names(datmeans)[1] <- datnames[i]
        plotdata <- as.data.frame(cbind(row.names(datmeans), datmeans[, 1], datmeans$std, as.character(datmeans$groups)))
        names(plotdata) <- c("Treat", "y", "std", "groups")
        plotdata$y <- as.numeric(as.character(plotdata$y))
        plotdata$std <- as.numeric(as.character(plotdata$std))
        plotdata$times <- n
        allplotdata <- rbind(allplotdata, plotdata)
        print(allplotdata)
    }
    theplot <- ggplot(data = allplotdata, mapping = aes(x = factor(times), y = y, fill = Treat)) + geom_bar(stat = 'identity', position = position_dodge(0.9), width = 0.7)  + labs(title = datnames[i], x = "Samples", y= datnames[i]) + geom_errorbar(aes(ymin = y - std, ymax = y + std), width = 0.2, position=position_dodge(0.9)) + ylim(min(0,min(allplotdata$y)-max(allplotdata$std)), max(max(allplotdata$y)+max(allplotdata$std), max(allplotdata$y) * 1.2)) + geom_text(mapping = aes(y = y + std, label = groups), position = position_dodge(0.9), vjust = -1)
    print(theplot)
    #dev.off()
}
dev.off()
