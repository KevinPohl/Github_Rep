from pandas import DataFrame

df = DataFrame({"tag": ["abc", "def"],
                "patterns": ["hi", "bye"],
                "responses": ["ho", "bo"]
                })

print(f"df\n{df}\n\n")

df_new = (df
          [["tag", "responses"]]
          [df["responses"]=="bo"]
          .loc[df["patterns"]=="bye"]
          .loc[df["tag"] == "def"]
          )

# alternative as one-liner next to each other
df_new = df[["tag", "responses"]][df["responses"]=="bo"].loc[df["patterns"]=="bye"].loc[df["tag"] == "def"]

# # alternative with userwarning
# df_new = (df
#           [["tag", "responses"]]
#           [df["responses"]=="bo"]
#           [df["patterns"]=="bye"]
#           [df["tag"] == "def"]
#           )

df_new = (df
          [(df["responses"] == "bo") | (df["responses"] == "ho")]
          [df["tag"] == "def"]

          .loc[df["tag"] == "def"]
          .loc[df["tag"] == "def"]
          [["tag", "responses"]]
          # following creates an error because | is executed at higher order than ==, fix by putting in () or .isin()
          # [df["responses"]==2020 | df["responses"]==2022 | df["responses"]==2024] # error
          .loc[(df["responses"]==2020) | (df["responses"]==2022) | (df["responses"]==2024)]
          .loc[df["responses"].isin([2020, 2022, 2024])]
          # .loc prefix is to suppress "UserWarning: Boolean Series key will be reindexed to match DataFrame index."
          # when a filter in one or more columns leads to reindexing (= one or more rows are filtered out completely)
          # so selection of columns is not affected
          )

# alternative with userwarning
# df_new = (df
#           [(df["responses"] == "bo") | (df["responses"] == "ho")]
#           [df["tag"] == "def"]
#           [df["tag"] == "def"]
#           [df["tag"] == "def"]
#           [["tag", "responses"]]
#           [(df["responses"]==2020) | (df["responses"]==2022) | (df["responses"]==2024)]
#           [df["responses"].isin([2020, 2022, 2024])]
#           )

# advanced, pipelined slicing with string method contains
df_new = (df
          .loc[df["tag"].isin(["abc", "def"])] # filter rows based on values in column tag
          .loc[df["patterns"].isin(["hi", "bye"])] # filter rows based on values in column patterns
          # .loc is optional here, because no reindexing occurs in this case (UserWarning won't show either way)
          # filter columns based on column name containing letter t using str methods like startswith, endswith and contains
          .iloc[:, df.columns.str.contains("t")]
          # this works, because a boolean mask is made and used, in this case ["tag", "patterns", "responses"] is searched
          # for .str.contains("t") which gives [True, True, False], this is then used as .iloc[:, [True, True, False]]
          # .loc[:, "tag"] # filter columns on name tag afterwards, effectively filtering out column patterns
          .loc[:, ["tag"]] # alternative writing, must for multiple columns
          # ["tag"] # alternative writing
          # [["tag"]] # alternative writing, must for multiple columns
          )


# some rules:
# order of filter in row values DOES NOT matter, this
df_new = df[(df["responses"] == "bo") | (df["responses"] == "ho")][df["tag"] == "def"]
# is the same as this
df_new = df[df["tag"] == "def"][(df["responses"] == "bo") | (df["responses"] == "ho")]
          
# order of column selection DOES matter, this will work
df_new = df[["tag", "responses"]]["tag"]
# # this does not
# df_new = df["tag"][["tag", "responses"]]
# because first, a subset containing only tag is made, then a column responses is to be produced based off
# of that "out of thin air", which doesn't work


print(f"df_new\n{df_new}\n\n")




