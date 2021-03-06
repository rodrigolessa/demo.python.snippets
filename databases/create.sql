USE [figura]
GO

IF OBJECT_ID('dbo.VisualTrees', 'U') IS NOT NULL 
  DROP TABLE dbo.VisualTrees;

CREATE TABLE [dbo].[VisualTrees](
	[Id] [int] IDENTITY(1,1) NOT NULL,
	[Name] [varchar](255) NOT NULL,
	[Label] [int] NOT NULL,
 CONSTRAINT [PK_VisualTrees] PRIMARY KEY CLUSTERED 
(
	[Id] ASC
)WITH (PAD_INDEX  = OFF, STATISTICS_NORECOMPUTE  = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS  = ON, ALLOW_PAGE_LOCKS  = ON) ON [PRIMARY]
) ON [PRIMARY]

GO

SET ANSI_PADDING OFF
GO