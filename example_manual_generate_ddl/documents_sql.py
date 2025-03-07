# documents.py

from uuid import uuid4
from langchain.docstore.document import Document

# Buat list dokumen sql
sql_documents = [
    # Definisikan dokumen-dokumen sql
    Document(
        page_content="""Question: Daerah mana yang memiliki angka stunting tertinggi?
        SQL Query:
        SELECT kk.nama_kabupaten_kota, ps.prevalensi_balita_stunting, ps.tahun
        FROM prevalensi_balita_stunting_per_kab_kota ps
        JOIN kabupaten_kota kk ON ps.kode_kabupaten_kota = kk.kode_kabupaten_kota AND kk.kode_provinsi = 32
        JOIN (SELECT MAX(tahun) AS max_tahun FROM prevalensi_balita_stunting_per_kab_kota) AS max_ps ON ps.tahun = max_ps.max_tahun
        ORDER BY ps.prevalensi_balita_stunting DESC
        LIMIT 5;""",
        metadata={"source": "sql"},
    ),

    Document(
        page_content="""Question: Berapa angka stunting di Jawa Barat tahun 2023?
        SQL Query:
        SELECT nama_provinsi, AVG(prevalensi_balita_stunting) AS prevalensi_balita_stunting, sumber, tahun FROM provinsi pr
        INNER JOIN kabupaten_kota kk ON kk.kode_provinsi = pr.kode_provinsi AND pr.kode_provinsi = 32
        LEFT JOIN prevalensi_balita_stunting_per_kab_kota pv ON pv.kode_kabupaten_kota = kk.kode_kabupaten_kota AND pv.tahun = 2023
        GROUP BY nama_provinsi, sumber, tahun;""",
        metadata={"source": "sql"},
    ),

    Document(
        page_content="""Question: Berapa jumlah balita stunting di Jawa Barat tahun 2024?
        SQL Query:
        SELECT nama_provinsi, SUM(jumlah_balita_stunting) AS jumlah_balita_stunting, tahun 
        FROM provinsi pr
        INNER JOIN kabupaten_kota kk ON kk.kode_provinsi = pr.kode_provinsi AND pr.kode_provinsi = 32
        LEFT JOIN jumlah_balita_stunting_per_kab_kota js ON js.kode_kabupaten_kota = kk.kode_kabupaten_kota AND js.tahun = 2024
        GROUP BY nama_provinsi, tahun;""",
        metadata={"source": "sql"},
    ),

    Document(
        page_content="""Question: Berapa jumlah ibu hamil di Jawa Barat?
        SQL Query:
        SELECT nama_provinsi, SUM(jumlah_ibu_hamil) AS jumlah_ibu_hamil, tahun 
        FROM provinsi pr
        INNER JOIN kabupaten_kota kk ON kk.kode_provinsi = pr.kode_provinsi AND pr.kode_provinsi = 32
        LEFT JOIN jumlah_bumil_per_kab_kota jb ON jb.kode_kabupaten_kota = kk.kode_kabupaten_kota
        GROUP BY nama_provinsi, tahun
        ORDER BY tahun DESC
        LIMIT 5;""",
        metadata={"source": "sql"},
    ),

    Document(
        page_content="""Question: Berapa jumlah ibu hamil bermasalah gizi di Jawa Barat?
        SQL Query:
        SELECT prov.nama_provinsi, anemia.jumlah_ibu_hamil_anemia, kek.jumlah_ibu_hamil_kurangan_energi_kronis, COALESCE(anemia.tahun, kek.tahun) AS tahun
        FROM (SELECT SUM(jumlah_ibu_hamil_anemia) AS jumlah_ibu_hamil_anemia, k.kode_provinsi, tahun
            FROM jumlah_bumil_anemia_per_kab_kota j
            JOIN kabupaten_kota k ON j.kode_kabupaten_kota = k.kode_kabupaten_kota AND k.kode_provinsi = 32
            GROUP BY k.kode_provinsi, tahun) anemia
        FULL OUTER JOIN (SELECT SUM(jumlah_ibu_hamil_kek) AS jumlah_ibu_hamil_kurangan_energi_kronis, k.kode_provinsi, tahun
            FROM jumlah_bumil_kurangan_energi_kronis_per_triwulan_per_kab_kota j
            JOIN kabupaten_kota k ON j.kode_kabupaten_kota = k.kode_kabupaten_kota AND k.kode_provinsi = 32
            GROUP BY k.kode_provinsi, tahun) kek
        ON anemia.tahun = kek.tahun AND anemia.kode_provinsi = kek.kode_provinsi
        JOIN provinsi prov ON COALESCE(anemia.kode_provinsi, kek.kode_provinsi) = prov.kode_provinsi
        ORDER BY tahun DESC;""",
        metadata={"source": "sql"},
    ),

    Document(
        page_content="""Question: Berapa jumlah remaja putri di Jawa Barat?
        SQL Query:
        SELECT nama_provinsi, SUM(jumlah_remaja_putri) AS jumlah_remaja_putri, tahun
        FROM provinsi pr
        INNER JOIN kabupaten_kota kk ON kk.kode_provinsi = pr.kode_provinsi AND pr.kode_provinsi = 32
        LEFT JOIN jumlah_remaja_putri_per_triwulan_per_kab_kota jr ON jr.kode_kabupaten_kota = kk.kode_kabupaten_kota
        GROUP BY nama_provinsi, tahun
        ORDER BY tahun DESC
        LIMIT 5;""",
        metadata={"source": "sql"},
    ),

    Document(
        page_content="""Question: Berapa jumlah remaja putri anemia di Jawa Barat?
        SQL Query:
        SELECT nama_provinsi, SUM(jumlah_remaja_putri_anemia) AS jumlah_remaja_putri_anemia, tahun
        FROM provinsi pr
        INNER JOIN kabupaten_kota kk ON kk.kode_provinsi = pr.kode_provinsi AND pr.kode_provinsi = 32
        LEFT JOIN jumlah_remaja_putri_anemia_per_kab_kota ja ON ja.kode_kabupaten_kota = kk.kode_kabupaten_kota
        GROUP BY nama_provinsi, tahun
        ORDER BY tahun DESC
        LIMIT 5;""",
        metadata={"source": "sql"},
    ),

    Document(
        page_content="""Question: Berapa jumlah remaja putri anemia di Jawa Barat?
        SQL Query:
        SELECT nama_provinsi, SUM(jumlah_remaja_putri_anemia) AS jumlah_remaja_putri_anemia, tahun
        FROM provinsi pr
        INNER JOIN kabupaten_kota kk ON kk.kode_provinsi = pr.kode_provinsi AND pr.kode_provinsi = 32
        LEFT JOIN jumlah_remaja_putri_anemia_per_kab_kota ja ON ja.kode_kabupaten_kota = kk.kode_kabupaten_kota
        GROUP BY nama_provinsi, tahun
        ORDER BY tahun DESC
        LIMIT 5;""",
        metadata={"source": "sql"},
    ),

    Document(
        page_content="""Question: Bagaimana tren angka stunting di Jawa Barat dalam 3 tahun terakhir?
        SQL Query:
        SELECT AVG(ps.prevalensi_balita_stunting) AS avg_prevalensi_stunting, ps.tahun
        FROM prevalensi_balita_stunting_per_kab_kota ps JOIN kabupaten_kota kk ON ps.kode_kabupaten_kota = kk.kode_kabupaten_kota AND kk.kode_provinsi = 32 
        GROUP BY tahun 
        ORDER BY tahun DESC LIMIT 3;""",
        metadata={"source": "sql"},
    ),

    Document(
        page_content="""Question: Berapa jumlah keluarga yang beresiko atau rentan stunting di Jawa Barat?
        SQL Query:
        SELECT SUM(jumlah_keluarga_rentan_stunting) AS jumlah_keluarga_rentan_stunting, tahun
        FROM keluarga_rentan_stunting_per_desa krs 
        JOIN kabupaten_kota kk ON krs.kode_kabupaten_kota = kk.kode_kabupaten_kota AND kk.kode_provinsi = 32 
        GROUP BY tahun 
        ORDER BY tahun DESC;""",
        metadata={"source": "sql"},
    ),

    Document(
        page_content="""Question: Bandingkan data stunting provinsi Jawa Barat dengan Kota Bandung
        SQL Query:
        SELECT avg_data.prevalensi_balita_stunting AS avg_prevalensi_balita_stunting_provinsi,
			bandung_data.prevalensi_balita_stunting AS prevalensi_balita_stunting_bandung,
			COALESCE(avg_data.tahun, bandung_data.tahun) AS tahun
        FROM (SELECT AVG(prevalensi_balita_stunting) AS prevalensi_balita_stunting, tahun
			FROM prevalensi_balita_stunting_per_kab_kota pv 
			JOIN kabupaten_kota kk ON pv.kode_kabupaten_kota = kk.kode_kabupaten_kota 
			WHERE kk.kode_provinsi = 32
			GROUP BY tahun) avg_data
        LEFT JOIN (SELECT prevalensi_balita_stunting, tahun
			FROM prevalensi_balita_stunting_per_kab_kota pv
			JOIN kabupaten_kota kk ON pv.kode_kabupaten_kota = kk.kode_kabupaten_kota 
			WHERE kk.nama_kabupaten_kota = 'KOTA BANDUNG') bandung_data
        ON avg_data.tahun = bandung_data.tahun
        ORDER BY tahun DESC;""",
        metadata={"source": "sql"},
    ),

    Document(
        page_content="""Question: Sebaran balita stunting di Kota Bandung
        SQL Query:
        SELECT jb.nama_kabupaten_kota, jb.bps_nama_kecamatan, jb.bps_nama_desa_kelurahan, jb.nama_puskesmas, jb.jumlah_balita_stunting, jb.periode, jb.tahun 
        FROM jumlah_balita_stunting_per_desa jb
        JOIN (SELECT MAX(tahun) AS max_tahun FROM jumlah_balita_stunting_per_desa) AS max_ps ON jb.tahun = max_ps.max_tahun AND jb.nama_kabupaten_kota = 'KOTA BANDUNG';""",
        metadata={"source": "sql"},
    ),

    Document(
        page_content="""Question: Kabupaten/kota mana di Jawa Barat yang memiliki angka stunting tertinggi?
        SQL Query:
        SELECT kk.nama_kabupaten_kota, ps.prevalensi_balita_stunting, ps.tahun
        FROM prevalensi_balita_stunting_per_kab_kota ps
        JOIN kabupaten_kota kk ON ps.kode_kabupaten_kota = kk.kode_kabupaten_kota AND kk.kode_provinsi = 32
        JOIN (SELECT MAX(tahun) AS max_tahun FROM prevalensi_balita_stunting_per_kab_kota) AS max_ps ON ps.tahun = max_ps.max_tahun
        ORDER BY ps.prevalensi_balita_stunting DESC
        LIMIT 1;""",
        metadata={"source": "sql"},
    ),

    Document(
        page_content="""Question: Berapa anggaran panurunan stunting di Jawa Barat?
        SQL Query:
        SELECT pr.nama_provinsi, SUM(ra.anggaran) AS total_anggaran, ra.tahun_pelaksanaan FROM rincian_kegiatan_dan_anggaran_stunting_dalam_rencana_kerja ra
        LEFT JOIN kabupaten_kota kk ON kk.kode_kabupaten_kota = ra.kode_kabupaten_kota 
        LEFT JOIN provinsi pr ON pr.kode_provinsi = kk.kode_provinsi AND pr.kode_provinsi = 32
        GROUP BY pr.nama_provinsi, ra.tahun_pelaksanaan
        ORDER BY tahun_pelaksanaan DESC;""",
        metadata={"source": "sql"},
    ),

    Document(
        page_content="""Question: Berapa anggaran panurunan stunting per kabupaten kota di Jawa Barat?
        SQL Query:
        SELECT kk.nama_kabupaten_kota, SUM(ra.anggaran) AS jumlah_anggaran, ra.tahun_pelaksanaan FROM rincian_kegiatan_dan_anggaran_stunting_dalam_rencana_kerja ra
        LEFT JOIN kabupaten_kota kk ON kk.kode_kabupaten_kota = ra.kode_kabupaten_kota 
        LEFT JOIN provinsi pr ON pr.kode_provinsi = kk.kode_provinsi AND pr.kode_provinsi = 32
        GROUP BY kk.nama_kabupaten_kota, ra.tahun_pelaksanaan
        ORDER BY tahun_pelaksanaan DESC;""",
        metadata={"source": "sql"},
    ),

    Document(
        page_content="""Question: Berapa anggaran panurunan stunting di Kota Bogor?
        SQL Query:
        SELECT kk.nama_kabupaten_kota, SUM(ra.anggaran) AS total_anggaran, ra.tahun_pelaksanaan
        FROM rincian_kegiatan_dan_anggaran_stunting_dalam_rencana_kerja ra
        INNER JOIN kabupaten_kota kk ON kk.kode_kabupaten_kota = ra.kode_kabupaten_kota AND kk.nama_kabupaten_kota = 'KOTA BOGOR'
        GROUP BY kk.nama_kabupaten_kota, ra.tahun_pelaksanaan
        ORDER BY ra.tahun_pelaksanaan;""",
        metadata={"source": "sql"},
    ),

    Document(
        page_content="""Question: Berapa anggaran panurunan stunting per kegiatan di Kota Bandung?
        SQL Query:
        SELECT kk.nama_kabupaten_kota, ra.rekomendasi AS kegiatan, SUM(ra.anggaran) AS jumlah_anggaran, ra.tahun_pelaksanaan
        FROM rincian_kegiatan_dan_anggaran_stunting_dalam_rencana_kerja ra
        INNER JOIN kabupaten_kota kk ON kk.kode_kabupaten_kota = ra.kode_kabupaten_kota AND kk.nama_kabupaten_kota = 'KOTA BANDUNG'
        GROUP BY kk.nama_kabupaten_kota, kegiatan, ra.tahun_pelaksanaan
        ORDER BY ra.tahun_pelaksanaan;""",
        metadata={"source": "sql"},
    ),

]

# Generate UUIDs untuk setiap dokumen
sql_uuids = [str(uuid4()) for _ in range(len(sql_documents))]
