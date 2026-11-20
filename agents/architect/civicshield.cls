% ==============================================================================
% civicshield.cls - Custom Government-Tender LuaLaTeX Book Class
% Project: CivicShield AI Preliminary Report
% Engine: LuaLaTeX (Mandatory for clean BiDi Hebrew/English & OpenType fonts)
% ==============================================================================
\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{civicshield}[2026/11/20 v1.0 CivicShield AI State-Engineering Report Class]

\DeclareOption*{\PassOptionsToClass{\CurrentOption}{book}}
\ProcessOptions\relax
\LoadClass[11pt,a4paper,twoside,openany]{book}

% --- Core LuaLaTeX & BiDi Packages --------------------------------------------
\RequirePackage{iftex}
\RequireLuaTeX

\RequirePackage{fontspec}
\RequirePackage[bidi=basic,layout=tabular]{babel}
\babelprovide[import,main]{hebrew}
\babelprovide[import]{english}

% --- Typography (Safe Fallbacks for Windows/Linux TeX Live) -------------------
\IfFontExistsTF{David CLM}{
  \babelfont[hebrew]{rm}{David CLM}
  \babelfont[hebrew]{sf}{Simple CLM}
  \babelfont[hebrew]{tt}{Miriam Mono CLM}
}{
  \IfFontExistsTF{Frank Ruhl Libre}{
    \babelfont[hebrew]{rm}{Frank Ruhl Libre}
    \babelfont[hebrew]{sf}{Heebo}
    \babelfont[hebrew]{tt}{DejaVu Sans Mono}
  }{
    \babelfont[hebrew]{rm}{Arial}
    \babelfont[hebrew]{sf}{Arial}
    \babelfont[hebrew]{tt}{Courier New}
  }
}

\IfFontExistsTF{Liberation Serif}{
  \babelfont[english]{rm}{Liberation Serif}
  \babelfont[english]{sf}{Liberation Sans}
  \babelfont[english]{tt}{Liberation Mono}
}{
  \babelfont[english]{rm}{DejaVu Serif}
  \babelfont[english]{sf}{DejaVu Sans}
  \babelfont[english]{tt}{DejaVu Sans Mono}
}

% --- Page Geometry ------------------------------------------------------------
\RequirePackage[
  a4paper,
  top=26mm,
  bottom=24mm,
  inner=24mm,
  outer=20mm,
  headheight=15mm,
  headsep=7mm,
  footskip=11mm
]{geometry}

\RequirePackage{setspace}
\onehalfspacing
\setlength{\parskip}{5pt}
\setlength{\parindent}{0pt}

% --- State-Engineering Color Palette ------------------------------------------
\RequirePackage[table,svgnames]{xcolor}

\definecolor{CSNavy}{HTML}{0B1F3A}       % Primary Sovereign Navy
\definecolor{CSSlate}{HTML}{1E3A5F}      % Secondary Engineering Slate
\definecolor{CSGold}{HTML}{B8860B}       % Sovereign Gold Accent
\definecolor{CSSteel}{HTML}{4A5568}      % Neutral Technical Gray
\definecolor{CSIce}{HTML}{F4F7FA}        % Subtle Surface Tint
\definecolor{CSBorder}{HTML}{CBD5E0}     % Clean Hairline Border
\definecolor{CSRiskRed}{HTML}{9B2C2C}    % Risk / Alert Crimson
\definecolor{CSRiskBg}{HTML}{FFF5F5}     % Risk Background Tint
\definecolor{CSInsightTeal}{HTML}{1E6B52}% Insight / Architecture Emerald
\definecolor{CSInsightBg}{HTML}{F0FAF6}  % Insight Background Tint
\definecolor{CSContractBg}{HTML}{FBF8F1} % Contract / SLA Warm Tint

% --- Graphics, TikZ, Tables, Math & Hyperlinks --------------------------------
\RequirePackage{amsmath,amssymb}
\RequirePackage{booktabs,array,longtable,tabularx,multirow}
\RequirePackage{enumitem}
\RequirePackage{tikz}
\usetikzlibrary{
  arrows.meta,
  positioning,
  shapes.geometric,
  shapes.multipart,
  fit,
  backgrounds,
  calc,
  shadows.blur,
  decorations.pathreplacing
}
\RequirePackage[most]{tcolorbox}
\RequirePackage{titlesec}
\RequirePackage{fancyhdr}
\RequirePackage{lastpage}
\RequirePackage[
  colorlinks=true,
  linkcolor=CSSlate,
  citecolor=CSInsightTeal,
  urlcolor=CSNavy,
  bookmarks=true
]{hyperref}

% --- Clean BiDi Helpers -------------------------------------------------------
\newcommand{\en}[1]{\foreignlanguage{english}{#1}}
\newcommand{\code}[1]{\foreignlanguage{english}{\texttt{\small\color{CSSlate}#1}}}

\newenvironment{ltrblock}{%
  \par\begin{otherlanguage}{english}%
}{%
  \end{otherlanguage}\par%
}

\newtcblisting{ltrcode}[1][]{
  enhanced,
  breakable,
  colback=CSIce,
  colframe=CSSlate,
  leftrule=3pt,
  rightrule=0.5pt,
  toprule=0.5pt,
  bottomrule=0.5pt,
  arc=2pt,
  listing only,
  listing options={
    basicstyle=\ttfamily\footnotesize\color{CSNavy},
    breaklines=true,
    columns=flexible
  },
  before upper={\begin{otherlanguage}{english}},
  after upper={\end{otherlanguage}},
  #1
}

% --- Custom Callout Boxes (Insight, Risk, Contract) ---------------------------
\newtcolorbox{insightbox}[1][תובנה ארכיטקטונית]{
  enhanced,
  breakable,
  colback=CSInsightBg,
  colframe=CSInsightTeal,
  coltitle=white,
  fonttitle=\sffamily\bfseries\normalsize,
  title={#1},
  attach boxed title to top right={xshift=-4mm,yshift=-2.5mm},
  boxed title style={
    colback=CSInsightTeal,
    arc=2pt,
    boxrule=0pt
  },
  leftrule=0.8pt,
  rightrule=3.5pt,
  toprule=0.8pt,
  bottomrule=0.8pt,
  arc=2pt,
  top=4mm,
  bottom=3mm,
  left=4mm,
  right=4mm,
  before skip=10pt,
  after skip=10pt
}

\newtcolorbox{riskbox}[1][סיכון קריטי ובקרת נגד]{
  enhanced,
  breakable,
  colback=CSRiskBg,
  colframe=CSRiskRed,
  coltitle=white,
  fonttitle=\sffamily\bfseries\normalsize,
  title={#1},
  attach boxed title to top right={xshift=-4mm,yshift=-2.5mm},
  boxed title style={
    colback=CSRiskRed,
    arc=2pt,
    boxrule=0pt
  },
  leftrule=0.8pt,
  rightrule=3.5pt,
  toprule=0.8pt,
  bottomrule=0.8pt,
  arc=2pt,
  top=4mm,
  bottom=3mm,
  left=4mm,
  right=4mm,
  before skip=10pt,
  after skip=10pt
}

\newtcolorbox{contractbox}[1][חוזה ממשק ו-SLA]{
  enhanced,
  breakable,
  colback=CSContractBg,
  colframe=CSGold,
  coltitle=CSNavy,
  fonttitle=\sffamily\bfseries\normalsize,
  title={#1},
  attach boxed title to top right={xshift=-4mm,yshift=-2.5mm},
  boxed title style={
    colback=CSGold!25!white,
    colframe=CSGold,
    arc=2pt,
    boxrule=0.8pt
  },
  leftrule=0.8pt,
  rightrule=3.5pt,
  toprule=0.8pt,
  bottomrule=0.8pt,
  arc=2pt,
  top=4mm,
  bottom=3mm,
  left=4mm,
  right=4mm,
  before skip=10pt,
  after skip=10pt
}

% --- Styled Chapter & Section Headers (No Default LaTeX Styling) --------------
\titleformat{\chapter}[display]
  {\normalfont\sffamily}
  {%
    \begin{tcolorbox}[
      enhanced,
      colback=CSNavy,
      colframe=CSNavy,
      arc=0pt,
      boxrule=0pt,
      left=5mm,right=5mm,top=3mm,bottom=3mm,
      borderline south={2.5pt}{0pt}{CSGold}
    ]
      \color{CSGold}\bfseries\large פרק \thechapter
    \end{tcolorbox}%
  }
  {-2pt}
  {%
    \begin{tcolorbox}[
      enhanced,
      colback=CSIce,
      colframe=CSBorder,
      arc=0pt,
      boxrule=0.5pt,
      left=5mm,right=5mm,top=4mm,bottom=4mm
    ]
      \color{CSNavy}\bfseries\LARGE
  }
  [\end{tcolorbox}]

\titlespacing*{\chapter}{0pt}{-12pt}{16pt}

\titleformat{\section}
  {\sffamily\Large\bfseries\color{CSNavy}}
  {\colorbox{CSSlate}{\color{white}\;\thesection\;}}
  {0.6em}
  {}
  [\vspace{2pt}{\color{CSGold}\titlerule[1pt]}]

\titleformat{\subsection}
  {\sffamily\large\bfseries\color{CSSlate}}
  {\thesubsection}
  {0.6em}
  {}

\titleformat{\subsubsection}
  {\sffamily\normalsize\bfseries\color{CSSteel}}
  {\thesubsubsection}
  {0.5em}
  {}

% --- Distinct Headers & Footers -----------------------------------------------
\newcommand{\CSDocCode}{CS-AI-PRELIM-2026-01}
\newcommand{\CSClassification}{סיווג: שמור -- טיוטת מכרז ממשלתי}

\fancypagestyle{mainstyle}{
  \fancyhf{}
  \fancyhead[R]{\sffamily\footnotesize\bfseries\color{CSNavy}\leftmark}
  \fancyhead[L]{\sffamily\footnotesize\color{CSSteel}\en{CivicShield AI} \;|\; \en{\CSDocCode}}
  \fancyfoot[R]{\sffamily\footnotesize\color{CSRiskRed}\CSClassification}
  \fancyfoot[L]{\sffamily\footnotesize\bfseries\color{CSNavy}עמוד \thepage\ מתוך \pageref{LastPage}}
  \renewcommand{\headrulewidth}{1pt}
  \renewcommand{\headrule}{\hbox to\headwidth{\color{CSGold}\leaders\hrule height \headrulewidth\hfill}}
  \renewcommand{\footrulewidth}{0.5pt}
  \renewcommand{\footrule}{\hbox to\headwidth{\color{CSBorder}\leaders\hrule height \footrulewidth\hfill}}
}

\fancypagestyle{plain}{
  \fancyhf{}
  \fancyfoot[R]{\sffamily\footnotesize\color{CSRiskRed}\CSClassification}
  \fancyfoot[L]{\sffamily\footnotesize\bfseries\color{CSNavy}עמוד \thepage\ מתוך \pageref{LastPage}}
  \renewcommand{\headrulewidth}{0pt}
  \renewcommand{\footrulewidth}{0.5pt}
  \renewcommand{\footrule}{\hbox to\headwidth{\color{CSBorder}\leaders\hrule height \footrulewidth\hfill}}
}

\pagestyle{mainstyle}

% --- Table Styling Defaults ---------------------------------------------------
\renewcommand{\arraystretch}{1.28}
\rowcolors{2}{CSIce}{white}

% --- Cover Page Command -------------------------------------------------------
\newcommand{\makecivicshieldcover}[4]{%
  % #1 = Title, #2 = Subtitle, #3 = Tender/Doc ID, #4 = Date & Version
  \begin{titlepage}
    \thispagestyle{empty}
    \begin{tikzpicture}[remember picture,overlay]
      % Top Navy Banner
      \fill[CSNavy] (current page.north west) rectangle ([yshift=-8.5cm]current page.north east);
      % Gold Accent Strip
      \fill[CSGold] ([yshift=-8.5cm]current page.north west) rectangle ([yshift=-8.85cm]current page.north east);
      % Subtle Geometric Grid on Banner
      \draw[white,opacity=0.07,step=0.8cm] (current page.north west) grid ([yshift=-8.5cm]current page.north east);
      % Bottom Footer Bar
      \fill[CSIce] (current page.south west) rectangle ([yshift=2.6cm]current page.south east);
      \draw[CSBorder,line width=0.8pt] ([yshift=2.6cm]current page.south west) -- ([yshift=2.6cm]current page.south east);
    \end{tikzpicture}

    \vspace*{1.2cm}
    \begin{flushright}
      {\sffamily\bfseries\color{CSGold}\large מערך הדיגיטל והבינה המלאכותית הממשלתי}\\[0.6cm]
      {\sffamily\bfseries\color{white}\fontsize{30}{36}\selectfont #1}\\[0.5cm]
      {\sffamily\color{CSIce}\Large #2}
    \end{flushright}

    \vspace{4.2cm}

    \begin{tcolorbox}[
      enhanced,
      colback=white,
      colframe=CSSlate,
      leftrule=4pt,
      rightrule=4pt,
      arc=2pt,
      drop shadow
    ]
      \sffamily
      \textbf{\color{CSNavy}מזהה מסמך ומכרז:} \en{#3} \\[4pt]
      \textbf{\color{CSNavy}גרסה ותאריך:} #4 \\[4pt]
      \textbf{\color{CSNavy}סטטוס:} דוח ראשוני להערכת היתכנות וארכיטקטורה (\en{Preliminary Design Report}) \\[4pt]
      \textbf{\color{CSNavy}סיווג ביטחוני:} {\color{CSRiskRed}\textbf{\CSClassification}}
    \end{tcolorbox}

    \vfill
    \begin{flushright}
      \sffamily\footnotesize\color{CSSteel}
      הופק באמצעות ארכיטקטורת התיעוד ההנדסי של \en{CivicShield AI} --- כל הזכויות שמורות למדינת ישראל / צוות ההנדסה.
    \end{flushright}
  \end{titlepage}
}
