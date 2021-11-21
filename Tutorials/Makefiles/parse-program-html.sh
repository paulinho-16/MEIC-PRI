#!/bin/bash

# Print STDIN contents
cat - |

# Insert a newline after each </td> element so that each course is in an independent line
sed 's/<\/td>/<\/td>\n/g' |

# Match the lines with each course
awk '/ocorrencia_id\=[[:digit:]]/ {print $0}' |

# Use sed to extract course id and name
# -n is for ommiting non matching lines
# p flag prints the line where a match is made
sed -n 's,.*pv_ocorrencia_id=\([0-9]*\)">\([^\<]*\).*,\1\t\2,p' |

# Remove duplicate lines and output the result to STDOUT
sort -n | uniq