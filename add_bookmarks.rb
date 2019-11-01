require 'webloc'
require 'sqlite3'
require 'digest/sha2'


begin
  db = SQLite3::Database.new "bookmarks.db"

  bookmarks = Dir.glob('add_to_bookmarks/*.webloc')

  bookmarks.each do |b|
    name = File.basename(b, '.webloc')
    url = Webloc.load(b).url
    hash = Digest::SHA512.hexdigest(url)

    stm = db.prepare "SELECT 1 FROM bookmarks WHERE hash_key = ?"
    rs = stm.execute hash
    exists = rs.count > 0

    unless exists
      insert_stm = db.prepare "INSERT INTO bookmarks (title, url, hash_key) VALUES (?, ?, ?)"
      insert_stm.execute name, url, hash
      puts "URL: #{url} Inserted"
    end

  end

rescue  SQLite3::Exception => error
  puts "Exception occurred"
  puts error
end
