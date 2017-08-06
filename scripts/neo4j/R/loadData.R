#' @title load Data
#' @import dplyr
#' @description Funcao para carregar dados de Folha de Pagamento
#' @author Equipe Folha Limpa
#' @return Carrega dados para popular banco de grafos
#' @export
loadData <- function() {

  # Arquivos localizados na pasta data
  arqCargosMunicipio <- "data/cargosMunicipio.csv"
  arqMunicipio <- "data/TCE-PB-SAGRES-Folha_Pessoal_Esfera_Municipal.txt"
  arqEstado <- "data/TCE-PB-SAGRES-Folha_Pessoal_Esfera_Estadual.txt"
  arqDadosUnidadeGestora <- "data/dadosUnidadeGestoraMunicipais.csv"
  cargosMunicipio <- read.csv2(arqCargosMunicipio)
  dadosMunicipio <- read.csv2(arqMunicipio)
  dadosMunicipioAbril2017 <- dadosMunicipio %>% filter(dt_MesAnoReferencia == "42017")
  dadosMunicipioAbril2017 <- merge(x = dadosMunicipioAbril2017, y = cargosMunicipio, by = "de_cargo")
  dadosMunicipioAbril2017 <- merge(x = dadosMunicipioAbril2017, y = dadosUgestora, by = "de_ugestora")
  dadosMunicipioAbril2017 <- dadosMunicipioAbril2017[,c(-3,-4,-10)]
  colnames(dadosMunicipioAbril2017) <- c("CARGO","TP_CARGO","CPF","MESANO","NOME_SERVIDOR","VALOR","ORGAO", "CATEGORIA")
  dadosCargosEstadual <- "data/cargosEstadual.csv"
  cargosEstado <- read.csv(dadosCargosEstadual)
  dadosEstado <- read.csv2(arqEstado, sep = "|")
  dadosEstado <- dadosEstado[,c(-1,-8)]
  dadosEstadoAbril2017 <- dadosEstado %>% filter(dt_mesano == "42017")
  dadosEstadoAbril2017 <- merge(x = dadosEstadoAbril2017, y = cargosEstado, by = "no_cargo")
  MUNICIPIO <- array(1:nrow(dadosEstadoAbril2017))
  dadosEstadoAbril2017 <- cbind(dadosEstadoAbril2017,MUNICIPIO)
  colnames(dadosEstadoAbril2017) <- c("CARGO","ORGAO","TP_CARGO","CPF","NOME","MESANO","VALOR","CATEGORIA","MUNICIPIO")
  dadosEstadoAbril2017 <- dadosEstadoAbril2017[,c(2,1,3,4,6,5,7,8,9)]
  dadosAbril2017 <- rbind(dadosMunicipioAbril2017,dadosEstadoAbril2017)
  dadosMesAnalise <- dadosAbril2017
  dadosMesAnalise$VALOR <- as.numeric(dadosMesAnalise$VALOR)
  # Acima de um salario Minimo
  dadosMesAnalise <- dadosMesAnalise %>% filter(VALOR > 937)
  '%!in%' <- function(x,y)!('%in%'(x,y))
  dadosAgrupadosCPF <- dadosMesAnalise %>% group_by(CPF)
  dadosAgrupadosCPF <- summarise(dadosAgrupadosCPF, n = n())
  # somente servidores com mais de dois vinculos
  dadosServidoresMaisVinculos <- dadosAgrupadosCPF %>% filter(n > 1)
  dadosMesAnalise <- dadosMesAnalise %>% filter(CPF %in% dadosServidoresMaisVinculos$CPF)
  dadosAcumulados <- merge(x = dadosMesAnalise, y = dadosServidoresMaisVinculos, by = "CPF")
  # Removendo situações que permitem mais de um vinculo
  cargosPermitem2Vinculos <- c("PROFESSOR","MEDICO","ENFERMEIRO","DENTISTA","JUIZ","PROMOTOR","BIOMEDICO","SANITARISTA",
                               "FISIOTERAPEUTA","APOSENTADO","ODONTOLOGO","VEREADOR","PENSIONISTA","PSICOLOGO","MILITAR"
                               ,"FARMACEUTICO","AUX.DE ENFERMAGEM","BIOMEDICO SSA-ANS-601.2.1","NUTRICIONISTA","BIOQUIMICO",
                               "AUXILIAR DE ENFERMAGEM","AGENTE DE COMBATE A ENDEMIAS","FONOAUDIOLOGO",
                               "VETERINARIO","PEDAGOGO","PEDAGOGA","AUXILIAR DE ENSINO - QSM-901",
                               "AUX.DE ENFERMAGEM-EFE",
                            "DEFENSOR","DEPUTADO")
  dadosAcumuladosFinal <- dadosAcumulados %>% filter(CATEGORIA %in% cargosPermitem2Vinculos)
  dadosAcumuladosFinal <- dadosAcumuladosFinal %>% filter(n == 2)
  dadosExportarNeo4J <- dadosAcumulados %>% filter(CPF %!in% dadosAcumuladosFinal$CPF)
  write.csv(dadosExportarNeo4J,"dadosAcumulados.csv")
}
