CREATE TABLE escala_prestador (
  cd_escala_prestador  NUMBER(10,0) NOT NULL,
  cd_prestador         NUMBER(10,0) NOT NULL,
  semana               VARCHAR(10)  NOT NULL,
  dia                  VARCHAR(3)       NULL,
  dia_semana           VARCHAR(10)      NULL,
  mes                  VARCHAR(10)      NULL,
  ano                  VARCHAR(10)      NULL,
  ativo                VARCHAR(10)      NULL
)
  STORAGE (
    NEXT       1024 K
  )
/

COMMENT ON COLUMN escala_prestador.cd_escala_prestador     IS 'CODIGO PRIMARIO';
COMMENT ON COLUMN escala_prestador.cd_prestador            IS 'NOME DO PRESTADOR';
COMMENT ON COLUMN escala_prestador.semana                  IS 'SE PRESTADOR FOR INTEGRADO';
COMMENT ON COLUMN escala_prestador.dia                     IS 'DATA DE NASCIMENTO';
COMMENT ON COLUMN escala_prestador.dia_semana              IS 'CPF DO PRESTADOR';
COMMENT ON COLUMN escala_prestador.mes                     IS 'RG DO PRESTADOR';
COMMENT ON COLUMN escala_prestador.ano                     IS 'NUMERO DO CONSELHO DO PRESTADOR';
COMMENT ON COLUMN escala_prestador.ativo                   IS 'CHAVE ESTRANGEIRA DA ESPECIALIDADE';


CREATE SEQUENCE escala_prestador_seq
MINVALUE 1
MAXVALUE 9999999999
START WITH 1
INCREMENT BY 1
NOCACHE
NOCYCLE;



CREATE TABLE prestador (
  cd_prestador          NUMBER(10,0) NOT NULL,
  id_integrado          NUMBER(10,0) NOT NULL,
  nm_prestador          VARCHAR(40)  NOT NULL,
  nascimento            DATE             NULL,
  cd_tip_conselho       NUMBER(10,0)     NULL,
  conselho              VARCHAR(15)      NULL,
  cpf                   VARCHAR(12)      NULL,
  rg                    VARCHAR(10)      NULL,
  cns                   VARCHAR(20)      NULL,
  especialidade         VARCHAR(30)      NULL,
  ativo                 VARCHAR(2)       NULL
)
  STORAGE (
    NEXT       1024 K
  )
/
COMMENT ON COLUMN prestador.cd_prestador     IS 'CODIGO PRIMARIO';
COMMENT ON COLUMN prestador.nm_prestador     iS 'NOME DO PRESTADOR';
COMMENT ON COLUMN prestador.id_integrado     IS 'SE PRESTADOR FOR INTEGRADO';
COMMENT ON COLUMN prestador.nascimento       IS 'DATA DE NASCIMENTO';
COMMENT ON COLUMN prestador.cd_tip_conselho  IS 'TIPO DE CONSELHO';
COMMENT ON COLUMN prestador.conselho         IS 'CÓDIGO DO CONSELHO';
COMMENT ON COLUMN prestador.cns              IS 'CNS DO PRESTADOR';
COMMENT ON COLUMN prestador.cpf              IS 'CPF DO PRESTADOR';
COMMENT ON COLUMN prestador.rg               IS 'RG DO PRESTADOR';
COMMENT ON COLUMN prestador.especialidade    IS 'ESPECIALIDADE';
COMMENT ON COLUMN prestador.ativo            IS 'SE ATIVO';


CREATE SEQUENCE prestador_seq
MINVALUE 1
MAXVALUE 9999999999
START WITH 1
INCREMENT BY 1
NOCACHE
NOCYCLE;



CREATE TABLE reg_ent (
  cd_reg_ent   NUMBER(10,0) NOT NULL,
  cd_prestador NUMBER(10,0) NOT NULL,
  dt_reg_ent   DATE         NOT NULL,
  tp_reg_ent   VARCHAR2(3)  NULL
)
  STORAGE (
    NEXT       1024 K
  )
/

COMMENT ON COLUMN reg_ent.cd_reg_ent IS 'CODIGO PRIMARIO';
COMMENT ON COLUMN reg_ent.cd_prestador IS 'CODIGO ESTRANGEIRO TABELA PRESTADOR';
COMMENT ON COLUMN reg_ent.dt_reg_ent IS 'DATA DO REGISTRO';
COMMENT ON COLUMN reg_ent.tp_reg_ent IS 'TIPO DO REGISTRO SENDO E - ENTRADA / S - SAIDA';


CREATE SEQUENCE reg_ent_seq
MINVALUE 1
MAXVALUE 9999999999
START WITH 1
INCREMENT BY 1
NOCACHE
NOCYCLE;

