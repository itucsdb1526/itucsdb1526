Parts Implemented by Member Name
================================
kod ekleme

.. literalinclude:: ../server.py
    :language: python
    :lines: 12-40
    :emphasize-lines: 2


.. code-block:: python

	@app.route('/players/search/<key>')
	def players_search(key):
	    key = parse.unquote(key)
	    data = {"type": ('Player',), "Player": players.search(key)}
	    return render_template('search.html', key=key, data=data)

resim ekleme

.. figure:: main.png
   :scale: 30 %
   :alt: map to buried treasure

   This is the caption of the figure (a simple paragraph).