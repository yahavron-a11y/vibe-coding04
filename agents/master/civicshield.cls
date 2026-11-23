% ==============================================================================
% civicshield.cls - Executive Government-Tender LuaLaTeX Book Class (v2.0)
% Project: CivicShield AI Preliminary Report
% Engine: LuaLaTeX (Mandatory for clean BiDi Hebrew/English & OpenType fonts)
% ==============================================================================
\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{civicshield}[2026/11/20 v2.0 CivicShield AI Executive State-Engineering Report Class]

\DeclareOption*{\PassOptionsToClass{\CurrentOption}{book}}
\ProcessOptions\relax
\LoadClass[11pt,a4paper,twoside,openany]{book}

% --- Report Page Numbering (Arabic throughout, no Roman frontmatter) ----------
\renewcommand{\frontmatter}{%
  \clearpage
  \@mainmatterfalse
  \pagenumbering{arabic}%
}
\renewcommand{\mainmatter}{%
  \clearpage
  \@mainmattertrue
}

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
  \babelfont[english]{rm}{Times New Roman}
  \babelfont[english]{sf}{Arial}
  \babelfont[english]{tt}{Courier New}
}

% --- Page Geometry ------------------------------------------------------------
\RequirePackage[
  a4paper,
  top=26mm,
  bottom=25mm,
  inner=24mm,
  outer=20mm,
  headheight=15mm,
  headsep=7mm,
  footskip=12mm
]{geometry}

\RequirePackage{setspace}
\onehalfspacing
\setlength{\parskip}{5.5pt}
\setlength{\parindent}{0pt}
\setlength{\emergencystretch}{1.5em}
\raggedbottom
\widowpenalty=10000
\clubpenalty=10000

% --- State-Engineering Color Palette ------------------------------------------
\RequirePackage[table,svgnames]{xcolor}

\definecolor{CSNavy}{HTML}{0B1F3A}       % Primary Sovereign Navy
\definecolor{CSNavyDeep}{HTML}{061325}   % Deep Executive Navy
\definecolor{CSSlate}{HTML}{1E3A5F}      % Secondary Engineering Slate
\definecolor{CSGold}{HTML}{B8860B}       % Sovereign Gold Accent
\definecolor{CSGoldLight}{HTML}{D4AF37}  % Luminous Gold Highlight
\definecolor{CSSteel}{HTML}{4A5568}      % Neutral Technical Gray
\definecolor{CSIce}{HTML}{F4F7FA}        % Subtle Surface Tint
\definecolor{CSBorder}{HTML}{CBD5E0}     % Clean Hairline Border
\definecolor{CSRiskRed}{HTML}{9B2C2C}    % Risk / Alert Crimson
\definecolor{CSRiskBg}{HTML}{FFF5F5}     % Risk Background Tint
\definecolor{CSInsightTeal}{HTML}{1E6B52}% Insight / Architecture Emerald
\definecolor{CSInsightBg}{HTML}{F0FAF6}  % Insight Background Tint
\definecolor{CSContractBg}{HTML}{FBF8F1} % Contract / SLA Warm Tint

% --- Graphics, TikZ, Tables, Captions, Math & Hyperlinks ----------------------
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
\RequirePackage{needspace}
\RequirePackage{titlesec}
\RequirePackage{fancyhdr}
\RequirePackage{lastpage}
\RequirePackage[
  font={sf,small},
  labelfont={bf,sf,color=CSNavy},
  textfont={sf,color=CSSteel},
  labelsep=quad,
  skip=8pt
]{caption}
\RequirePackage[
  colorlinks=true,
  linkcolor=CSSlate,
  citecolor=CSInsightTeal,
  urlcolor=CSNavy,
  bookmarks=true
]{hyperref}

% --- Clean BiDi Helpers -------------------------------------------------------
\newcommand{\en}[1]{\foreignlanguage{english}{#1}}
\providecommand{\textenglish}[1]{\foreignlanguage{english}{#1}}
\providecommand{\LR}[1]{\foreignlanguage{english}{#1}}
\providecommand{\texthebrew}[1]{\foreignlanguage{hebrew}{#1}}
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
  leftrule=3.5pt,
  rightrule=0.5pt,
  toprule=0.5pt,
  bottomrule=0.5pt,
  arc=3pt,
  shadow={1mm}{-1mm}{0mm}{CSNavy!10},
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

% --- Upgraded Callout Boxes (Insight, Risk, Contract) -------------------------
\tcbset{
  civicrtl/.style={
    enhanced,
    before={\par\noindent\begingroup\pardir TLT\textdir TLT},
    after={\endgroup\par},
    before upper={\pardir TRT\textdir TRT},
    before lower={\pardir TRT\textdir TRT},
    before title={\pardir TRT\textdir TRT},
  }
}

\newtcolorbox{insightbox}[1][תובנה ארכיטקטונית]{
  civicrtl,
  colback=CSInsightBg,
  colframe=CSInsightTeal!85!black,
  coltitle=white,
  fonttitle=\sffamily\bfseries\small,
  title={#1},
  attach boxed title to top right={xshift=-5mm,yshift=-3.2mm},
  boxed title style={
    colback=CSInsightTeal,
    arc=9pt,
    boxrule=0pt,
    left=7pt,
    right=7pt,
    top=2.5pt,
    bottom=2.5pt,
    shadow={0.6mm}{-0.6mm}{0mm}{CSNavy!15}
  },
  leftrule=0.6pt,
  rightrule=4pt,
  toprule=0.6pt,
  bottomrule=0.6pt,
  arc=3.5pt,
  shadow={1.2mm}{-1.2mm}{0mm}{CSInsightTeal!12},
  top=5.5mm,
  bottom=4mm,
  left=5mm,
  right=5mm,
  before skip=12pt,
  after skip=12pt
}

\newtcolorbox{riskbox}[1][סיכון קריטי ובקרת נגד]{
  civicrtl,
  colback=CSRiskBg,
  colframe=CSRiskRed!85!black,
  coltitle=white,
  fonttitle=\sffamily\bfseries\small,
  title={#1},
  attach boxed title to top right={xshift=-5mm,yshift=-3.2mm},
  boxed title style={
    colback=CSRiskRed,
    arc=9pt,
    boxrule=0pt,
    left=7pt,
    right=7pt,
    top=2.5pt,
    bottom=2.5pt,
    shadow={0.6mm}{-0.6mm}{0mm}{CSNavy!15}
  },
  leftrule=0.6pt,
  rightrule=4pt,
  toprule=0.6pt,
  bottomrule=0.6pt,
  arc=3.5pt,
  shadow={1.2mm}{-1.2mm}{0mm}{CSRiskRed!12},
  top=5.5mm,
  bottom=4mm,
  left=5mm,
  right=5mm,
  before skip=12pt,
  after skip=12pt
}

\newtcolorbox{contractbox}[1][חוזה ממשק ו-SLA]{
  civicrtl,
  colback=CSContractBg,
  colframe=CSGold,
  coltitle=CSNavy,
  fonttitle=\sffamily\bfseries\small,
  title={#1},
  attach boxed title to top right={xshift=-5mm,yshift=-3.2mm},
  boxed title style={
    colback=CSGold!28!white,
    colframe=CSGold,
    arc=9pt,
    boxrule=0.8pt,
    left=7pt,
    right=7pt,
    top=2.5pt,
    bottom=2.5pt,
    shadow={0.6mm}{-0.6mm}{0mm}{CSNavy!12}
  },
  leftrule=0.6pt,
  rightrule=4pt,
  toprule=0.6pt,
  bottomrule=0.6pt,
  arc=3.5pt,
  shadow={1.2mm}{-1.2mm}{0mm}{CSGold!15},
  top=5.5mm,
  bottom=4mm,
  left=5mm,
  right=5mm,
  before skip=12pt,
  after skip=12pt
}

% --- Elevated Chapter & Section Headers (No Default LaTeX Styling) ------------
\titleformat{\chapter}[display]
  {\normalfont\sffamily}
  {%
    \begin{tcolorbox}[
      enhanced,
      interior style={left color=CSNavyDeep, right color=CSSlate},
      colframe=CSNavy,
      arc=3pt,
      rounded corners=north,
      boxrule=0pt,
      left=6mm,right=6mm,top=4mm,bottom=4mm,
      borderline south={3pt}{0pt}{CSGold},
      overlay={
        \begin{scope}[opacity=0.10]
          \draw[white, line width=0.5pt]
            ([xshift=6mm]frame.south west) -- ([xshift=22mm]frame.north west)
            ([xshift=14mm]frame.south west) -- ([xshift=30mm]frame.north west)
            ([xshift=22mm]frame.south west) -- ([xshift=38mm]frame.north west);
          \draw[CSGoldLight, line width=0.7pt]
            ([xshift=10mm,yshift=4mm]frame.south west) circle (6mm);
        \end{scope}
      }
    ]
      \color{CSGoldLight}\bfseries\normalsize פרק\quad
      {\fontsize{28}{30}\selectfont\color{white}\thechapter}
    \end{tcolorbox}%
  }
  {-3pt}
  {%
    \begin{tcolorbox}[
      enhanced,
      colback=CSIce,
      colframe=CSBorder,
      arc=3pt,
      rounded corners=south,
      boxrule=0.6pt,
      left=6mm,right=6mm,top=5mm,bottom=5mm,
      shadow={1.2mm}{-1.2mm}{0mm}{CSNavy!10}
    ]
      \color{CSNavy}\bfseries\LARGE
  }
  [\end{tcolorbox}]

\titlespacing*{\chapter}{0pt}{-14pt}{18pt}

\titleformat{\section}
  {\needspace{5\baselineskip}\sffamily\Large\bfseries\color{CSNavy}}
  {\tcbox[on line, arc=3pt, colback=CSSlate, colframe=CSSlate, colupper=white, boxrule=0pt, left=4pt, right=4pt, top=1.5pt, bottom=1.5pt]{\thesection}}
  {0.6em}
  {}
  [\vspace{2.5pt}{\color{CSGold}\titlerule[1.2pt]}]

\titleformat{\subsection}
  {\needspace{4\baselineskip}\sffamily\large\bfseries\color{CSSlate}}
  {\color{CSGold}\thesubsection}
  {0.6em}
  {}

\titleformat{\subsubsection}
  {\needspace{3\baselineskip}\sffamily\normalsize\bfseries\color{CSSteel}}
  {\thesubsubsection}
  {0.5em}
  {}

% --- Distinct Headers & Footers with Pill Page Numbers ------------------------
\newcommand{\CSDocCode}{CS-AI-PRELIM-2026-01}
\newcommand{\CSClassification}{סיווג: שמור -- טיוטת מכרז ממשלתי}

\newtcbox{\CSPagePill}{
  on line,
  arc=7pt,
  colback=CSNavy,
  colframe=CSNavy,
  colupper=white,
  boxrule=0pt,
  left=6pt,
  right=6pt,
  top=2pt,
  bottom=2pt,
  fontupper=\sffamily\footnotesize\bfseries
}

\fancypagestyle{mainstyle}{
  \fancyhf{}
  \fancyhead[R]{\sffamily\footnotesize\bfseries\color{CSNavy}\leftmark}
  \fancyhead[L]{\sffamily\footnotesize\color{CSSteel}\en{CivicShield AI} \;{\color{CSGold}|}\; \en{\CSDocCode}}
  \fancyfoot[R]{\sffamily\footnotesize\bfseries\color{CSRiskRed}\CSClassification}
  \fancyfoot[L]{\CSPagePill{עמוד \thepage\ מתוך \pageref{LastPage}}}
  \renewcommand{\headrulewidth}{1pt}
  \renewcommand{\headrule}{\hbox to\headwidth{\color{CSGold}\leaders\hrule height \headrulewidth\hfill}}
  \renewcommand{\footrulewidth}{0.5pt}
  \renewcommand{\footrule}{\hbox to\headwidth{\color{CSBorder}\leaders\hrule height \footrulewidth\hfill}}
}

\fancypagestyle{plain}{
  \fancyhf{}
  \fancyfoot[R]{\sffamily\footnotesize\bfseries\color{CSRiskRed}\CSClassification}
  \fancyfoot[L]{\CSPagePill{עמוד \thepage\ מתוך \pageref{LastPage}}}
  \renewcommand{\headrulewidth}{0pt}
  \renewcommand{\footrulewidth}{0.5pt}
  \renewcommand{\footrule}{\hbox to\headwidth{\color{CSBorder}\leaders\hrule height \footrulewidth\hfill}}
}

\pagestyle{mainstyle}

% --- Table Styling Defaults ---------------------------------------------------
\renewcommand{\arraystretch}{1.28}
% \rowcolors{2}{CSIce}{white} % Disabled globally to avoid colortbl/TikZ stack overflow

% --- Rich Executive TikZ Cover Page Command -----------------------------------
\newcommand{\makecivicshieldcover}[4]{%
  % #1 = Title, #2 = Subtitle, #3 = Tender/Doc ID, #4 = Date & Version
  \begin{titlepage}
    \hypersetup{pageanchor=false}
    \thispagestyle{empty}
    \begingroup\pardir TLT\textdir TLT
    \begin{tikzpicture}[remember picture,overlay]
      % Layered Navy/Slate Gradient Banner
      \shade[top color=CSNavyDeep, bottom color=CSSlate, middle color=CSNavy]
        (current page.north west) rectangle ([yshift=-11.2cm]current page.north east);

      % Subtle Geometric Grid on Banner
      \draw[white, opacity=0.05, step=0.85cm]
        (current page.north west) grid ([yshift=-11.2cm]current page.north east);

      % Diagonal Gold & Slate Geometric Accent Lines
      \draw[CSGold, line width=1.4pt, opacity=0.55]
        ([yshift=-9.8cm]current page.north west) -- ([xshift=9cm,yshift=-11.2cm]current page.north west);
      \draw[CSGoldLight, line width=0.6pt, opacity=0.45]
        ([xshift=1.5cm]current page.north west) -- ([xshift=6.5cm,yshift=-11.2cm]current page.north west);

      % Crisp Double Gold Divider Strip
      \fill[CSGold] ([yshift=-11.2cm]current page.north west) rectangle ([yshift=-11.55cm]current page.north east);
      \fill[CSGoldLight!65!white] ([yshift=-11.65cm]current page.north west) rectangle ([yshift=-11.78cm]current page.north east);

      % Custom Vector Shield + Neural-Grid Emblem (Left Side of Banner)
      \begin{scope}[shift={([xshift=4.0cm, yshift=-5.7cm]current page.north west)}, scale=1.18]
        % Outer Glow Ring
        \draw[CSGoldLight, opacity=0.22, line width=0.8pt] (0,0) circle (2.35cm);
        \draw[white, opacity=0.14, dashed, line width=0.6pt] (0,0) circle (2.05cm);

        % Shield Outer Silhouette
        \path[
          draw=CSGoldLight, line width=1.8pt,
          top color=CSNavyDeep, bottom color=CSSlate!85!black,
          fill opacity=0.92
        ]
          (0, 1.85) -- (1.45, 1.25) -- (1.35, -0.35)
          .. controls (1.25, -1.25) and (0.55, -1.75) .. (0, -2.05)
          .. controls (-0.55, -1.75) and (-1.25, -1.25) .. (-1.35, -0.35)
          -- (-1.45, 1.25) -- cycle;

        % Inner Shield Trim
        \path[draw=white, opacity=0.35, line width=0.6pt]
          (0, 1.62) -- (1.24, 1.10) -- (1.16, -0.30)
          .. controls (1.07, -1.08) and (0.48, -1.52) .. (0, -1.78)
          .. controls (-0.48, -1.52) and (-1.07, -1.08) .. (-1.16, -0.30)
          -- (-1.24, 1.10) -- cycle;

        % Neural-Grid Edges inside Shield
        \coordinate (N0) at (0, 0.15);
        \coordinate (N1) at (0, 1.10);
        \coordinate (N2) at (0.82, 0.62);
        \coordinate (N3) at (0.76, -0.45);
        \coordinate (N4) at (0, -1.15);
        \coordinate (N5) at (-0.76, -0.45);
        \coordinate (N6) at (-0.82, 0.62);

        \draw[CSGoldLight, opacity=0.65, line width=0.75pt]
          (N1)--(N2)--(N3)--(N4)--(N5)--(N6)--(N1)
          (N0)--(N1) (N0)--(N2) (N0)--(N3) (N0)--(N4) (N0)--(N5) (N0)--(N6);

        % Neural Nodes
        \foreach \p in {N1,N2,N3,N4,N5,N6} {
          \fill[CSIce] (\p) circle (2.2pt);
          \draw[CSGoldLight, line width=0.7pt] (\p) circle (3.4pt);
        }
        \fill[CSGoldLight] (N0) circle (3.5pt);
        \draw[white, line width=0.8pt] (N0) circle (5.2pt);
      \end{scope}

      % Bottom Executive Footer Bar
      \fill[CSIce] (current page.south west) rectangle ([yshift=2.6cm]current page.south east);
      \draw[CSGold, line width=1pt] ([yshift=2.6cm]current page.south west) -- ([yshift=2.6cm]current page.south east);
    \end{tikzpicture}
    \endgroup

    \vspace*{1.5cm}
    \noindent\begin{minipage}{11.5cm}
      \raggedleft
      {\sffamily\bfseries\color{CSGoldLight}\large מערך הדיגיטל והבינה המלאכותית הממשלתי}\\[0.55cm]
      {\sffamily\bfseries\color{white}\fontsize{32}{38}\selectfont #1}\\[0.55cm]
      {\sffamily\color{CSIce}\Large #2}
    \end{minipage}

    \vspace{5.6cm}

    \begin{tcolorbox}[
      enhanced,
      colback=white,
      colframe=CSNavy,
      leftrule=1pt,
      rightrule=4.5pt,
      toprule=2.5pt,
      bottomrule=1pt,
      borderline north={2.5pt}{0pt}{CSGold},
      arc=3.5pt,
      top=5mm,
      bottom=5mm,
      left=6mm,
      right=6mm,
      shadow={1.8mm}{-1.8mm}{0mm}{CSNavy!14}
    ]
      \sffamily
      \textbf{\color{CSNavy}מזהה מסמך ומכרז:} \en{#3} \\[5pt]
      \textbf{\color{CSNavy}גרסה ותאריך:} #4 \\[5pt]
      \textbf{\color{CSNavy}סטטוס:} דוח ראשוני להערכת היתכנות וארכיטקטורה (\en{Preliminary Design Report}) \\[5pt]
      \textbf{\color{CSNavy}סיווג ביטחוני:} {\color{CSRiskRed}\textbf{\CSClassification}}
    \end{tcolorbox}

    \vfill
    \begin{flushright}
      \sffamily\footnotesize\color{CSSteel}
      הופק באמצעות ארכיטקטורת התיעוד ההנדסי של \en{CivicShield AI} --- כל הזכויות שמורות למדינת ישראל / צוות ההנדסה.
    \end{flushright}
  \end{titlepage}
  \hypersetup{pageanchor=true}
  \setcounter{page}{1}
}
