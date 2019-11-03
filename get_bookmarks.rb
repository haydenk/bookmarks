require 'sqlite3'
require 'csv'
require 'cgi'

begin
  db = SQLite3::Database.new "bookmarks.db"

  Dir.mkdir 'build'

  File.open('build/README.md', 'wb') do |file|
    file << "[CSV](bookmarks.csv)\n\n"
    stm = db.prepare "SELECT title, url FROM bookmarks"
    stm.execute.each do |row|
      title, url = row
      title = CGI.escape_html(title)
      file << "1. [#{title}](#{url})\n"
    end
  end

  CSV.open('build/bookmarks.csv', 'wb') do |csv|
    csv << %w(id title url)
    stm = db.prepare "SELECT id, title, url FROM bookmarks"
    stm.execute.each { |row| csv << row }
  end

rescue  SQLite3::Exception => error
  puts "Exception occurred"
  puts error
end
