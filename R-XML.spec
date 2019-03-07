#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-XML
Version  : 3.98.1.19
Release  : 61
URL      : https://cran.r-project.org/src/contrib/XML_3.98-1.19.tar.gz
Source0  : https://cran.r-project.org/src/contrib/XML_3.98-1.19.tar.gz
Summary  : Tools for Parsing and Generating XML Within R and S-Plus
Group    : Development/Tools
License  : BSD-2-Clause GPL-2.0
Requires: R-XML-lib = %{version}-%{release}
BuildRequires : buildreq-R
BuildRequires : libxml2-dev
BuildRequires : xmlsec1-dev
BuildRequires : xz-dev
BuildRequires : zlib-dev

%description
dataFrameEvent.R     example of closure for reading a data frame via the event based parser.
foo.dtd              DTD used for testing the DTD parsing facilities (getDTD()).
job.xml              example XML file taken from the libxml-1.7.3 examples.
enhancedDataFrame.R  version of the event-driven data frame reader with more error checking.

%package lib
Summary: lib components for the R-XML package.
Group: Libraries

%description lib
lib components for the R-XML package.


%prep
%setup -q -c -n XML

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1551930083

%install
export SOURCE_DATE_EPOCH=1551930083
rm -rf %{buildroot}
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library XML
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library XML
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library XML
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library XML|| : 
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/XML/COPYRIGHTS
/usr/lib64/R/library/XML/DESCRIPTION
/usr/lib64/R/library/XML/INDEX
/usr/lib64/R/library/XML/LICENSE
/usr/lib64/R/library/XML/Meta/Rd.rds
/usr/lib64/R/library/XML/Meta/features.rds
/usr/lib64/R/library/XML/Meta/hsearch.rds
/usr/lib64/R/library/XML/Meta/links.rds
/usr/lib64/R/library/XML/Meta/nsInfo.rds
/usr/lib64/R/library/XML/Meta/package.rds
/usr/lib64/R/library/XML/NAMESPACE
/usr/lib64/R/library/XML/R/XML
/usr/lib64/R/library/XML/R/XML.rdb
/usr/lib64/R/library/XML/R/XML.rdx
/usr/lib64/R/library/XML/exampleData/9003-en.html
/usr/lib64/R/library/XML/exampleData/9003.html
/usr/lib64/R/library/XML/exampleData/GNUmakefile
/usr/lib64/R/library/XML/exampleData/README
/usr/lib64/R/library/XML/exampleData/Rref.xml
/usr/lib64/R/library/XML/exampleData/Rsource.xml
/usr/lib64/R/library/XML/exampleData/SOAPNamespaces.xml
/usr/lib64/R/library/XML/exampleData/StatModel.dtd
/usr/lib64/R/library/XML/exampleData/TestInvalid.xml
/usr/lib64/R/library/XML/exampleData/allNodeTypes.xml
/usr/lib64/R/library/XML/exampleData/author.xml
/usr/lib64/R/library/XML/exampleData/author.xsd
/usr/lib64/R/library/XML/exampleData/author1.xml
/usr/lib64/R/library/XML/exampleData/author2.xml
/usr/lib64/R/library/XML/exampleData/author2.xsd
/usr/lib64/R/library/XML/exampleData/basic.xml
/usr/lib64/R/library/XML/exampleData/book.xml
/usr/lib64/R/library/XML/exampleData/boxplot.svg
/usr/lib64/R/library/XML/exampleData/branch.xml
/usr/lib64/R/library/XML/exampleData/catalog.xml
/usr/lib64/R/library/XML/exampleData/cdata.xml
/usr/lib64/R/library/XML/exampleData/charts.svg
/usr/lib64/R/library/XML/exampleData/cleanNamespace.xml
/usr/lib64/R/library/XML/exampleData/content.html
/usr/lib64/R/library/XML/exampleData/dataframe.xml
/usr/lib64/R/library/XML/exampleData/dot.xml
/usr/lib64/R/library/XML/exampleData/dtd.zip
/usr/lib64/R/library/XML/exampleData/entity.xml
/usr/lib64/R/library/XML/exampleData/entity1.xml
/usr/lib64/R/library/XML/exampleData/entity2.xml
/usr/lib64/R/library/XML/exampleData/entity3.html
/usr/lib64/R/library/XML/exampleData/entity4.xml
/usr/lib64/R/library/XML/exampleData/entityValue
/usr/lib64/R/library/XML/exampleData/eurofxref-hist.xml.gz
/usr/lib64/R/library/XML/exampleData/event.xml
/usr/lib64/R/library/XML/exampleData/foo.dtd
/usr/lib64/R/library/XML/exampleData/functionTemplate.xml
/usr/lib64/R/library/XML/exampleData/generalInfo.xml
/usr/lib64/R/library/XML/exampleData/gnumeric.xml
/usr/lib64/R/library/XML/exampleData/graph.gxl
/usr/lib64/R/library/XML/exampleData/iTunes.plist
/usr/lib64/R/library/XML/exampleData/include.xml
/usr/lib64/R/library/XML/exampleData/job.xml
/usr/lib64/R/library/XML/exampleData/kiva_lender.xml
/usr/lib64/R/library/XML/exampleData/largeText.xml
/usr/lib64/R/library/XML/exampleData/lists.html
/usr/lib64/R/library/XML/exampleData/literate.dtd
/usr/lib64/R/library/XML/exampleData/literate.xml
/usr/lib64/R/library/XML/exampleData/literate.xsl
/usr/lib64/R/library/XML/exampleData/literateFunction.xml
/usr/lib64/R/library/XML/exampleData/longitudinalData.xml
/usr/lib64/R/library/XML/exampleData/malformed.xml
/usr/lib64/R/library/XML/exampleData/mathml.dtd
/usr/lib64/R/library/XML/exampleData/mathml.xml
/usr/lib64/R/library/XML/exampleData/mathmlFuncCall.xml
/usr/lib64/R/library/XML/exampleData/mathmlInt.xml
/usr/lib64/R/library/XML/exampleData/mathmlMatrix.xml
/usr/lib64/R/library/XML/exampleData/mathmlQuadratic.xml
/usr/lib64/R/library/XML/exampleData/mathmlRoot.xml
/usr/lib64/R/library/XML/exampleData/mathmlScript.xml
/usr/lib64/R/library/XML/exampleData/mathmlSet.xml
/usr/lib64/R/library/XML/exampleData/mathmlSimple.xml
/usr/lib64/R/library/XML/exampleData/mathmlSphere.xml
/usr/lib64/R/library/XML/exampleData/mathmlSums.xml
/usr/lib64/R/library/XML/exampleData/matrixMult.xml
/usr/lib64/R/library/XML/exampleData/mtcars.xml
/usr/lib64/R/library/XML/exampleData/namespaceHandlers.xml
/usr/lib64/R/library/XML/exampleData/namespaces.xml
/usr/lib64/R/library/XML/exampleData/namespaces1.xml
/usr/lib64/R/library/XML/exampleData/namespaces2.xml
/usr/lib64/R/library/XML/exampleData/nodes.xml
/usr/lib64/R/library/XML/exampleData/nodes1.xml
/usr/lib64/R/library/XML/exampleData/nodes2.xml
/usr/lib64/R/library/XML/exampleData/nodes3.xml
/usr/lib64/R/library/XML/exampleData/nsAttrs.xml
/usr/lib64/R/library/XML/exampleData/plist.xml
/usr/lib64/R/library/XML/exampleData/raw.xml
/usr/lib64/R/library/XML/exampleData/redundantNS.xml
/usr/lib64/R/library/XML/exampleData/reparent.xml
/usr/lib64/R/library/XML/exampleData/rhelp.xsl
/usr/lib64/R/library/XML/exampleData/rxinclude.xml
/usr/lib64/R/library/XML/exampleData/same.xml
/usr/lib64/R/library/XML/exampleData/setInterval.xml
/usr/lib64/R/library/XML/exampleData/simple.plist
/usr/lib64/R/library/XML/exampleData/simple.xml
/usr/lib64/R/library/XML/exampleData/size.xml
/usr/lib64/R/library/XML/exampleData/size1.xml
/usr/lib64/R/library/XML/exampleData/size2.xml
/usr/lib64/R/library/XML/exampleData/size3.xml
/usr/lib64/R/library/XML/exampleData/solr.xml
/usr/lib64/R/library/XML/exampleData/something.xml
/usr/lib64/R/library/XML/exampleData/svg.xml
/usr/lib64/R/library/XML/exampleData/symslines.svg
/usr/lib64/R/library/XML/exampleData/tagnames.xml
/usr/lib64/R/library/XML/exampleData/test.xml
/usr/lib64/R/library/XML/exampleData/test1.xml
/usr/lib64/R/library/XML/exampleData/tides.xml
/usr/lib64/R/library/XML/exampleData/utf.xml
/usr/lib64/R/library/XML/exampleData/vars.xml
/usr/lib64/R/library/XML/exampleData/writeRS.S
/usr/lib64/R/library/XML/exampleData/writeRS.xml
/usr/lib64/R/library/XML/exampleData/xinclude/a.xml
/usr/lib64/R/library/XML/exampleData/xinclude/b.xml
/usr/lib64/R/library/XML/exampleData/xinclude/c.xml
/usr/lib64/R/library/XML/exampleData/xinclude/d.xml
/usr/lib64/R/library/XML/exampleData/xinclude/e.xml
/usr/lib64/R/library/XML/exampleData/xinclude/simple.xml
/usr/lib64/R/library/XML/exampleData/xinclude/top.xml
/usr/lib64/R/library/XML/exampleData/xpathTest.xml
/usr/lib64/R/library/XML/exampleData/xysize.svg
/usr/lib64/R/library/XML/exampleData/xyz.svg.gz
/usr/lib64/R/library/XML/examples/CIS.R
/usr/lib64/R/library/XML/examples/DiGIR.R
/usr/lib64/R/library/XML/examples/GNUmakefile
/usr/lib64/R/library/XML/examples/HTMLText.R
/usr/lib64/R/library/XML/examples/README
/usr/lib64/R/library/XML/examples/Rhelp.xml
/usr/lib64/R/library/XML/examples/RhelpArchive.xml
/usr/lib64/R/library/XML/examples/RhelpInfo.xml
/usr/lib64/R/library/XML/examples/SAXEntity.R
/usr/lib64/R/library/XML/examples/SSource.dtd
/usr/lib64/R/library/XML/examples/author.R
/usr/lib64/R/library/XML/examples/bondYields.R
/usr/lib64/R/library/XML/examples/bondsTables.R
/usr/lib64/R/library/XML/examples/catalog.R
/usr/lib64/R/library/XML/examples/connections.R
/usr/lib64/R/library/XML/examples/connections1.R
/usr/lib64/R/library/XML/examples/createTree.R
/usr/lib64/R/library/XML/examples/createTree1.R
/usr/lib64/R/library/XML/examples/dataFrameEvent.R
/usr/lib64/R/library/XML/examples/docbook.R
/usr/lib64/R/library/XML/examples/ecb.R
/usr/lib64/R/library/XML/examples/enhancedDataFrame.R
/usr/lib64/R/library/XML/examples/event.R
/usr/lib64/R/library/XML/examples/event.S
/usr/lib64/R/library/XML/examples/eventHandlers.R
/usr/lib64/R/library/XML/examples/faq.R
/usr/lib64/R/library/XML/examples/filterDataFrameEvent.R
/usr/lib64/R/library/XML/examples/foo.html
/usr/lib64/R/library/XML/examples/formals.xsl
/usr/lib64/R/library/XML/examples/functionIndex.Sxml
/usr/lib64/R/library/XML/examples/genericHandlers.R
/usr/lib64/R/library/XML/examples/generic_file.xml
/usr/lib64/R/library/XML/examples/getElements.S
/usr/lib64/R/library/XML/examples/gettingStarted.html
/usr/lib64/R/library/XML/examples/gettingStarted.xml
/usr/lib64/R/library/XML/examples/gnumericHandler.R
/usr/lib64/R/library/XML/examples/hashTree.R
/usr/lib64/R/library/XML/examples/iTunes.plist
/usr/lib64/R/library/XML/examples/index.html
/usr/lib64/R/library/XML/examples/internalNodes.S
/usr/lib64/R/library/XML/examples/internalXInclude.xml
/usr/lib64/R/library/XML/examples/itunes.R
/usr/lib64/R/library/XML/examples/itunes.xml
/usr/lib64/R/library/XML/examples/itunes.xsl
/usr/lib64/R/library/XML/examples/itunesSax.R
/usr/lib64/R/library/XML/examples/itunesSax1.R
/usr/lib64/R/library/XML/examples/itunesSax2.R
/usr/lib64/R/library/XML/examples/mathml.R
/usr/lib64/R/library/XML/examples/mathmlPlot.R
/usr/lib64/R/library/XML/examples/metlin.R
/usr/lib64/R/library/XML/examples/mexico.R
/usr/lib64/R/library/XML/examples/mexico.xml
/usr/lib64/R/library/XML/examples/mi1.R
/usr/lib64/R/library/XML/examples/modified_itunes_sax.R
/usr/lib64/R/library/XML/examples/namespaces.S
/usr/lib64/R/library/XML/examples/namespaces1.S
/usr/lib64/R/library/XML/examples/newNodes.R
/usr/lib64/R/library/XML/examples/oop.S
/usr/lib64/R/library/XML/examples/pi.xml
/usr/lib64/R/library/XML/examples/pmml.R
/usr/lib64/R/library/XML/examples/prompt.xml
/usr/lib64/R/library/XML/examples/promptXML.R
/usr/lib64/R/library/XML/examples/promptXML.Sxml
/usr/lib64/R/library/XML/examples/rcode.xml
/usr/lib64/R/library/XML/examples/rcode.xsl
/usr/lib64/R/library/XML/examples/redirection.R
/usr/lib64/R/library/XML/examples/reorder.xml
/usr/lib64/R/library/XML/examples/sbml.xml
/usr/lib64/R/library/XML/examples/sbmlSAX.S
/usr/lib64/R/library/XML/examples/schema.xsd
/usr/lib64/R/library/XML/examples/schemaEg.xml
/usr/lib64/R/library/XML/examples/schemas.xml
/usr/lib64/R/library/XML/examples/svg.R
/usr/lib64/R/library/XML/examples/tags.Sxml
/usr/lib64/R/library/XML/examples/trademe_cars.R
/usr/lib64/R/library/XML/examples/valueFilterDataFrameEvent.R
/usr/lib64/R/library/XML/examples/wordML.R
/usr/lib64/R/library/XML/examples/writeExamples.S
/usr/lib64/R/library/XML/examples/xml2tex.Sxml
/usr/lib64/R/library/XML/examples/xmlSource.R
/usr/lib64/R/library/XML/examples/xmlTags.xml
/usr/lib64/R/library/XML/examples/xmlTree.R
/usr/lib64/R/library/XML/examples/xpath.R
/usr/lib64/R/library/XML/examples/xpath.xml
/usr/lib64/R/library/XML/examples/yeast_small-01.xml
/usr/lib64/R/library/XML/help/AnIndex
/usr/lib64/R/library/XML/help/XML.rdb
/usr/lib64/R/library/XML/help/XML.rdx
/usr/lib64/R/library/XML/help/aliases.rds
/usr/lib64/R/library/XML/help/paths.rds
/usr/lib64/R/library/XML/html/00Index.html
/usr/lib64/R/library/XML/html/R.css
/usr/lib64/R/library/XML/libs/symbols.rds
/usr/lib64/R/library/XML/scripts/RSXML.bsh
/usr/lib64/R/library/XML/scripts/RSXML.bsh.in
/usr/lib64/R/library/XML/scripts/RSXML.csh
/usr/lib64/R/library/XML/scripts/RSXML.csh.in

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/XML/libs/XML.so
/usr/lib64/R/library/XML/libs/XML.so.avx2
/usr/lib64/R/library/XML/libs/XML.so.avx512
