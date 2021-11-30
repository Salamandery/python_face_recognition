CREATE TABLE contrato (
  cd_contrato          NUMBER(10,0) NOT NULL,
  cd_usuario           VARCHAR(10)  NOT NULL,
  descricao            VARCHAR(10)  NOT NULL,
  data_inicio          DATE         NOT NULL,
  data_final           DATE             NULL,
  valor_contrato       NUMBER(10,0)     NULL
)
  STORAGE (
    NEXT       1024 K
  )
/

COMMENT ON COLUMN contrato.cd_contrato    IS 'CODIGO DO CONTRATO';
COMMENT ON COLUMN contrato.cd_usuario     IS 'USUARIO QUE ADMINISTRAO CONTRATO';
COMMENT ON COLUMN contrato.descricao      IS 'DESCRICAO DO CONTRATO';
COMMENT ON COLUMN contrato.data_inicio    IS 'DATA DO INICIO DO CONTRATO';
COMMENT ON COLUMN contrato.data_final     IS 'DATA DO TERMINO DO CONTRATO';
COMMENT ON COLUMN contrato.valor_contrato IS 'VALOR DO CONTRATO'

CREATE SEQUENCE contrato_seq
MINVALUE 1
MAXVALUE 9999999999
START WITH 1
INCREMENT BY 1
NOCACHE
NOCYCLE;