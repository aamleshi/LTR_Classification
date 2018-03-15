library(protr)
library(dplyr)
seqs <- read.csv('sequences.csv', header=TRUE)

pseudos <- vector('character')
for (s in 1:length(seqs$Sequence)) {
# for (s in 1:1) {
  test_seq <- trimws(as.character(seqs$Sequence[s]))
  # pssm <- extractPSSM(test_seq, database.path = '../clean_nrdb.fas', iter=3, evalue=0.001, num.threads=12, silent=TRUE)
  pssm <- try(t(read.delim(paste0('pssms/pssm_', s-1))))
  if (inherits(pssm, "try-error")) {
    next
  }
  feature <- extractPSSMFeature(pssm)
  new_seq <- ''
  for (i in 1:nchar(test_seq)) {
    lower <- (i-1)*20 + 1 
    upper <- i*20
    sub_feature <- feature[lower:upper]
    sel_name <- names(sub_feature)[sub_feature == min(sub_feature)]
    base <- substr(sel_name, nchar(sel_name), nchar(sel_name))
    new_seq <- paste0(new_seq, base[1])
  }
  pseudos[s] = new_seq
}
seqs = mutate(.data=seqs, pseudo=pseudos)

write.csv(seqs, file="pseqs.csv")
