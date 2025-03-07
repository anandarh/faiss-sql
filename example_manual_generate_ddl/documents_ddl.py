# documents_ddl.py

from uuid import uuid4
from langchain.docstore.document import Document

# Buat list dokumen ddl
ddl_documents = [
    # Definisikan dokumen-dokumen ddl
    Document(
        page_content="""CREATE TABLE "public"."garis_kemiskinan_per_kab_kota" (
            "id" int4 NOT NULL DEFAULT nextval('garis_kemiskinan_per_kabupaten_kota_id_seq'::regclass),
            "kode_kabupaten_kota" int4 NOT NULL,
            "garis_kemiskinan" int4,
            "satuan" varchar(50) COLLATE "pg_catalog"."default",
            "tahun" int4,
            FOREIGN KEY (kode_kabupaten_kota) REFERENCES kabupaten_kota(kode_kabupaten_kota)
        );""",
        metadata={"source": "ddl"},
    ),

    Document(
        page_content="""CREATE TABLE "public"."garis_kemiskinan_provinsi" (
            "id" int4 NOT NULL DEFAULT nextval('garis_kemiskinan_provinsi_id_seq'::regclass),
            "kode_provinsi" int4 NOT NULL,
            "semester" varchar(50) COLLATE "pg_catalog"."default",
            "garis_kemiskinan" int4,
            "satuan" varchar(50) COLLATE "pg_catalog"."default",
            "tahun" int4,
            FOREIGN KEY (kode_provinsi) REFERENCES provinsi(kode_provinsi)
        );""",
        metadata={"source": "ddl"},
    ),

    Document(
        page_content="""CREATE TABLE "public"."indeks_ketahanan_pangan_per_desa" (
            "kode_kabupaten_kota" int4,
            "nama_kabupaten_kota" varchar(255) COLLATE "pg_catalog"."default",
            "bps_kode_kecamatan" int4,
            "bps_nama_kecamatan" varchar(255) COLLATE "pg_catalog"."default",
            "kemendagri_kode_kecamatan" varchar(255) COLLATE "pg_catalog"."default",
            "kemendagri_nama_kecamatan" varchar(255) COLLATE "pg_catalog"."default",
            "indeks_ketahanan_pangan" float8,
            "satuan" varchar(255) COLLATE "pg_catalog"."default",
            "tahun" int4
        );""",
        metadata={"source": "ddl"},
    ),

    Document(
        page_content="""CREATE TABLE "public"."jumlah_balita_bergizi_kurang_per_kab_kota" (
            "id" int4 NOT NULL DEFAULT nextval('jumlah_balita_bergizi_kurang_per_kab_kota_id_seq'::regclass),
            "kode_kabupaten_kota" int4 NOT NULL,
            "jumlah_balita" int4,
            "satuan" varchar(50) COLLATE "pg_catalog"."default",
            "tahun" int4,
            FOREIGN KEY (kode_kabupaten_kota) REFERENCES kabupaten_kota(kode_kabupaten_kota)
        );""",
        metadata={"source": "ddl"},
    ),

    Document(
        page_content="""CREATE TABLE "public"."jumlah_balita_diukur_per_triwulan_per_kab_kota" (
            "id" int4 NOT NULL DEFAULT nextval('jumlah_balita_diukur_per_triwulan_per_kab_kota_id_seq'::regclass),
            "kode_kabupaten_kota" int4 NOT NULL,
            "jumlah_balita_diukur" int4,
            "satuan" varchar(50) COLLATE "pg_catalog"."default",
            "triwulan" int4,
            "tahun" int4,
            FOREIGN KEY (kode_kabupaten_kota) REFERENCES kabupaten_kota(kode_kabupaten_kota)
        );""",
        metadata={"source": "ddl"},
    ),

    Document(
        page_content="""CREATE TABLE "public"."jumlah_balita_gizi_buruk_per_desa" (
            "kode_kabupaten_kota" int4,
            "nama_kabupaten_kota" varchar(255) COLLATE "pg_catalog"."default",
            "bps_kode_kecamatan" int4,
            "bps_nama_kecamatan" varchar(255) COLLATE "pg_catalog"."default",
            "bps_kode_desa_kelurahan" int8,
            "bps_nama_desa_kelurahan" varchar(255) COLLATE "pg_catalog"."default",
            "kemendagri_kode_kecamatan" varchar(255) COLLATE "pg_catalog"."default",
            "kemendagri_nama_kecamatan" varchar(255) COLLATE "pg_catalog"."default",
            "kemendagri_kode_desa_kelurahan" varchar(255) COLLATE "pg_catalog"."default",
            "kemendagri_nama_desa_kelurahan" varchar(255) COLLATE "pg_catalog"."default",
            "kode_puskesmas" varchar(255) COLLATE "pg_catalog"."default",
            "nama_puskesmas" varchar(255) COLLATE "pg_catalog"."default",
            "jumlah_balita_gizi_buruk" int4,
            "satuan" varchar(255) COLLATE "pg_catalog"."default",
            "periode" varchar(255) COLLATE "pg_catalog"."default",
            "tahun" int4
        );""",
        metadata={"source": "ddl"},
    ),

    Document(
        page_content="""CREATE TABLE "public"."jumlah_balita_per_kategori_balita_gizi_buruk_per_kab_kota" (
            "id" int4 NOT NULL DEFAULT nextval('jumlah_balita_per_kategori_balita_gizi_buruk_per_kab_kot_id_seq'::regclass),
            "kode_kabupaten_kota" int4 NOT NULL,
            "kategori_gizi_buruk" varchar(50) COLLATE "pg_catalog"."default",
            "jumlah_balita" int4,
            "satuan" varchar(50) COLLATE "pg_catalog"."default",
            "tahun" int4,
            FOREIGN KEY (kode_kabupaten_kota) REFERENCES kabupaten_kota(kode_kabupaten_kota)
        );""",
        metadata={"source": "ddl"},
    ),

    Document(
        page_content="""CREATE TABLE "public"."jumlah_balita_stunting_per_desa" (
            "kode_kabupaten_kota" int4,
            "nama_kabupaten_kota" varchar(255) COLLATE "pg_catalog"."default",
            "bps_kode_kecamatan" int4,
            "bps_nama_kecamatan" varchar(255) COLLATE "pg_catalog"."default",
            "bps_kode_desa_kelurahan" int8,
            "bps_nama_desa_kelurahan" varchar(255) COLLATE "pg_catalog"."default",
            "kemendagri_kode_kecamatan" varchar(255) COLLATE "pg_catalog"."default",
            "kemendagri_nama_kecamatan" varchar(255) COLLATE "pg_catalog"."default",
            "kemendagri_kode_desa_kelurahan" varchar(255) COLLATE "pg_catalog"."default",
            "kemendagri_nama_desa_kelurahan" varchar(255) COLLATE "pg_catalog"."default",
            "kode_puskesmas" varchar(255) COLLATE "pg_catalog"."default",
            "nama_puskesmas" varchar(255) COLLATE "pg_catalog"."default",
            "jumlah_balita_stunting" int4,
            "satuan" varchar(255) COLLATE "pg_catalog"."default",
            "periode" varchar(255) COLLATE "pg_catalog"."default",
            "tahun" int4,
            FOREIGN KEY (kode_kabupaten_kota) REFERENCES kabupaten_kota(kode_kabupaten_kota)
            );""",
        metadata={"source": "ddl"},
    ),

    Document(
        page_content="""CREATE TABLE "public"."jumlah_balita_stunting_per_kab_kota" (
            "id" int4 NOT NULL DEFAULT nextval('jumlah_balita_stunting_per_kabupaten_kota_id_seq'::regclass),
            "kode_kabupaten_kota" int4 NOT NULL,
            "jumlah_balita_stunting" int4,
            "satuan" varchar(50) COLLATE "pg_catalog"."default",
            "tahun" int4,
            "periode" varchar(255) COLLATE "pg_catalog"."default",
            FOREIGN KEY (kode_kabupaten_kota) REFERENCES kabupaten_kota(kode_kabupaten_kota)
        );""",
        metadata={"source": "ddl"},
    ),

    Document(
        page_content="""CREATE TABLE "public"."jumlah_balita_underweight_per_desa" (
            "kode_kabupaten_kota" int4,
            "nama_kabupaten_kota" varchar(255) COLLATE "pg_catalog"."default",
            "bps_kode_kecamatan" int4,
            "bps_nama_kecamatan" varchar(255) COLLATE "pg_catalog"."default",
            "bps_kode_desa_kelurahan" int8,
            "bps_nama_desa_kelurahan" varchar(255) COLLATE "pg_catalog"."default",
            "kemendagri_kode_kecamatan" varchar(255) COLLATE "pg_catalog"."default",
            "kemendagri_nama_kecamatan" varchar(255) COLLATE "pg_catalog"."default",
            "kemendagri_kode_desa_kelurahan" varchar(255) COLLATE "pg_catalog"."default",
            "kemendagri_nama_desa_kelurahan" varchar(255) COLLATE "pg_catalog"."default",
            "kode_puskesmas" varchar(255) COLLATE "pg_catalog"."default",
            "nama_puskesmas" varchar(255) COLLATE "pg_catalog"."default",
            "jumlah_balita_underweight" int4,
            "satuan" varchar(255) COLLATE "pg_catalog"."default",
            "periode" varchar(255) COLLATE "pg_catalog"."default",
            "tahun" int4
        );""",
        metadata={"source": "ddl"},
    ),

    Document(
        page_content="""CREATE TABLE "public"."jumlah_balita_wasting_per_desa" (
            "kode_kabupaten_kota" int4,
            "nama_kabupaten_kota" varchar(255) COLLATE "pg_catalog"."default",
            "bps_kode_kecamatan" int4,
            "bps_nama_kecamatan" varchar(255) COLLATE "pg_catalog"."default",
            "bps_kode_desa_kelurahan" int8,
            "bps_nama_desa_kelurahan" varchar(255) COLLATE "pg_catalog"."default",
            "kemendagri_kode_kecamatan" varchar(255) COLLATE "pg_catalog"."default",
            "kemendagri_nama_kecamatan" varchar(255) COLLATE "pg_catalog"."default",
            "kemendagri_kode_desa_kelurahan" varchar(255) COLLATE "pg_catalog"."default",
            "kemendagri_nama_desa_kelurahan" varchar(255) COLLATE "pg_catalog"."default",
            "kode_puskesmas" varchar(255) COLLATE "pg_catalog"."default",
            "nama_puskesmas" varchar(255) COLLATE "pg_catalog"."default",
            "jumlah_balita_wasting" int4,
            "satuan" varchar(255) COLLATE "pg_catalog"."default",
            "periode" varchar(255) COLLATE "pg_catalog"."default",
            "tahun" int4
        );""",
        metadata={"source": "ddl"},
    ),

    Document(
        page_content="""CREATE TABLE "public"."jumlah_bayi_dapat_asi_per_puskesmas" (
            "kode_kabupaten_kota" int4,
            "nama_kabupaten_kota" varchar(255) COLLATE "pg_catalog"."default",
            "bps_kode_kecamatan" int4,
            "bps_nama_kecamatan" varchar(255) COLLATE "pg_catalog"."default",
            "kemendagri_kode_kecamatan" varchar(255) COLLATE "pg_catalog"."default",
            "kemendagri_nama_kecamatan" varchar(255) COLLATE "pg_catalog"."default",
            "kode_puskesmas" varchar(255) COLLATE "pg_catalog"."default",
            "nama_puskesmas" varchar(255) COLLATE "pg_catalog"."default",
            "asi_6bln_jml_bayi_asi_eksklusif" int4,
            "satuan" varchar(255) COLLATE "pg_catalog"."default",
            "periode" varchar(255) COLLATE "pg_catalog"."default",
            "tahun" int4
        );""",
        metadata={"source": "ddl"},
    ),

    Document(
        page_content="""CREATE TABLE "public"."jumlah_bidan_puskesmas_per_kab_kota" (
            "id" int4 NOT NULL DEFAULT nextval('jumlah_bidan_puskesmas_per_kab_kota_id_seq'::regclass),
            "kode_kabupaten_kota" int4 NOT NULL,
            "jumlah_bidan_puskesmas" int4,
            "satuan" varchar(10) COLLATE "pg_catalog"."default",
            "tahun" int4,
            FOREIGN KEY (kode_kabupaten_kota) REFERENCES kabupaten_kota(kode_kabupaten_kota)
        );""",
        metadata={"source": "ddl"},
    ),

    Document(
        page_content="""CREATE TABLE "public"."jumlah_bumil_anemia_per_kab_kota" (
            "id" int4 NOT NULL DEFAULT nextval('jumlah_bumil_anemia_per_kab_kota_id_seq'::regclass),
            "kode_kabupaten_kota" int4 NOT NULL,
            "jumlah_ibu_hamil_anemia" int4,
            "satuan" varchar(10) COLLATE "pg_catalog"."default",
            "tahun" int4,
            "periode" varchar(255) COLLATE "pg_catalog"."default",
            FOREIGN KEY (kode_kabupaten_kota) REFERENCES kabupaten_kota(kode_kabupaten_kota)
        );""",
        metadata={"source": "ddl"},
    ),

    Document(
        page_content="""CREATE TABLE "public"."jumlah_bumil_anemia_per_puskesmas" (
            "kode_kabupaten_kota" int4,
            "nama_kabupaten_kota" varchar(255) COLLATE "pg_catalog"."default",
            "bps_kode_kecamatan" int4,
            "bps_nama_kecamatan" varchar(255) COLLATE "pg_catalog"."default",
            "kemendagri_kode_kecamatan" varchar(255) COLLATE "pg_catalog"."default",
            "kemendagri_nama_kecamatan" varchar(255) COLLATE "pg_catalog"."default",
            "kode_puskesmas" varchar(255) COLLATE "pg_catalog"."default",
            "nama_puskesmas" varchar(255) COLLATE "pg_catalog"."default",
            "jumlah_ibu_hamil_anemia" int4,
            "satuan" varchar(255) COLLATE "pg_catalog"."default",
            "periode" varchar(255) COLLATE "pg_catalog"."default",
            "tahun" int4
        );""",
        metadata={"source": "ddl"},
    ),

    Document(
        page_content="""CREATE TABLE "public"."jumlah_bumil_dapat_makanan_tambahan_per_triwulan_per_kab_kota" (
            "id" int4 NOT NULL DEFAULT nextval('jumlah_bumil_dapat_makanan_tambahan_per_triwulan_per_kab_id_seq'::regclass),
            "kode_kabupaten_kota" int4 NOT NULL,
            "jumlah_ibu_hamil_pmt" int4,
            "satuan" varchar(50) COLLATE "pg_catalog"."default",
            "triwulan" int4,
            "tahun" int4,
            FOREIGN KEY (kode_kabupaten_kota) REFERENCES kabupaten_kota(kode_kabupaten_kota)
        );""",
        metadata={"source": "ddl"},
    ),

    Document(
        page_content="""CREATE TABLE "public"."jumlah_bumil_dapat_zat_besi_per_kab_kota" (
            "id" int4 NOT NULL DEFAULT nextval('jumlah_bumil_dapat_zat_besi_per_kab_kota_id_seq'::regclass),
            "kode_kabupaten_kota" int4 NOT NULL,
            "jenis_tablet" varchar(10) COLLATE "pg_catalog"."default",
            "jumlah_bumil" int4,
            "satuan" varchar(10) COLLATE "pg_catalog"."default",
            "tahun" int4,
            FOREIGN KEY (kode_kabupaten_kota) REFERENCES kabupaten_kota(kode_kabupaten_kota)
        );""",
        metadata={"source": "ddl"},
    ),

    Document(
        page_content="""CREATE TABLE "public"."jumlah_bumil_kurangan_energi_kronis_per_puskesmas" (
            "kode_kabupaten_kota" int4,
            "nama_kabupaten_kota" varchar(255) COLLATE "pg_catalog"."default",
            "bps_kode_kecamatan" int4,
            "bps_nama_kecamatan" varchar(255) COLLATE "pg_catalog"."default",
            "kemendagri_kode_kecamatan" varchar(255) COLLATE "pg_catalog"."default",
            "kemendagri_nama_kecamatan" varchar(255) COLLATE "pg_catalog"."default",
            "kode_puskesmas" varchar(255) COLLATE "pg_catalog"."default",
            "nama_puskesmas" varchar(255) COLLATE "pg_catalog"."default",
            "ibu_hamil_kek" int4,
            "satuan" varchar(255) COLLATE "pg_catalog"."default",
            "periode" varchar(255) COLLATE "pg_catalog"."default",
            "tahun" int4
        );""",
        metadata={"source": "ddl"},
    ),

    Document(
        page_content="""CREATE TABLE "public"."jumlah_bumil_kurangan_energi_kronis_per_triwulan_per_kab_kota" (
            "id" int4 NOT NULL DEFAULT nextval('jumlah_bumil_kurangan_energi_kronis_per_triwulan_per_kab_id_seq'::regclass),
            "kode_kabupaten_kota" int4 NOT NULL,
            "jumlah_ibu_hamil_kek" int4,
            "satuan" varchar(50) COLLATE "pg_catalog"."default",
            "triwulan" int4,
            "tahun" int4,
            FOREIGN KEY (kode_kabupaten_kota) REFERENCES kabupaten_kota(kode_kabupaten_kota)
        );""",
        metadata={"source": "ddl"},
    ),

    Document(
        page_content="""CREATE TABLE "public"."jumlah_bumil_penerima_imunisasi_tetanus_diphtheria_per_kab_kota" (
            "id" int4 NOT NULL DEFAULT nextval('jumlah_bumil_penerima_imunisasi_tetanus_diphtheria_per_k_id_seq'::regclass),
            "kode_kabupaten_kota" int4 NOT NULL,
            "jenis_imunisasi" varchar(10) COLLATE "pg_catalog"."default",
            "jumlah_penerima" int4,
            "satuan" varchar(10) COLLATE "pg_catalog"."default",
            "tahun" int4,
            FOREIGN KEY (kode_kabupaten_kota) REFERENCES kabupaten_kota(kode_kabupaten_kota)
        );""",
        metadata={"source": "ddl"},
    ),

    Document(
        page_content="""CREATE TABLE "public"."jumlah_bumil_penerima_tab_tambah_darah_per_kab_kota" (
            "id" int4 NOT NULL DEFAULT nextval('jumlah_bumil_penerima_tab_tambah_darah_per_kab_kota_id_seq'::regclass),
            "kode_kabupaten_kota" int4 NOT NULL,
            "jumlah_penerima_ttd" int4,
            "satuan" varchar(10) COLLATE "pg_catalog"."default",
            "tahun" int4,
            FOREIGN KEY (kode_kabupaten_kota) REFERENCES kabupaten_kota(kode_kabupaten_kota)
        );""",
        metadata={"source": "ddl"},
    ),

    Document(
        page_content="""CREATE TABLE "public"."jumlah_bumil_per_kab_kota" (
            "id" int4 NOT NULL DEFAULT nextval('jumlah_ibu_hamil_per_kabupaten_kota_id_seq'::regclass),
            "kode_kabupaten_kota" int4 NOT NULL,
            "jumlah_ibu_hamil" int4,
            "satuan" varchar(50) COLLATE "pg_catalog"."default",
            "tahun" int4,
            FOREIGN KEY (kode_kabupaten_kota) REFERENCES kabupaten_kota(kode_kabupaten_kota)
        );""",
        metadata={"source": "ddl"},
    ),

    Document(
        page_content="""CREATE TABLE "public"."jumlah_bumil_ukur_lingkar_lengan_atas_per_triwulan_per_kab_kota" (
            "id" int4 NOT NULL DEFAULT nextval('jumlah_bumil_ukur_lingkar_lengan_atas_per_triwulan_per_k_id_seq'::regclass),
            "kode_kabupaten_kota" int4 NOT NULL,
            "jumlah_ibu_hamil_lila" int4,
            "satuan" varchar(50) COLLATE "pg_catalog"."default",
            "triwulan" int4,
            "tahun" int4,
            FOREIGN KEY (kode_kabupaten_kota) REFERENCES kabupaten_kota(kode_kabupaten_kota)
        );""",
        metadata={"source": "ddl"},
    ),

    Document(
        page_content="""CREATE TABLE "public"."jumlah_calon_pengantin_diperiksa_per_gender_per_kab_kota" (
            "id" int4 NOT NULL DEFAULT nextval('jumlah_calon_pengantin_diperiksa_per_gender_per_kab_kota_id_seq'::regclass),
            "kode_kabupaten_kota" int4 NOT NULL,
            "jenis_kelamin" varchar(50) COLLATE "pg_catalog"."default",
            "jumlah_catin_dilayani" int4,
            "satuan" varchar(10) COLLATE "pg_catalog"."default",
            "tahun" int4,
            FOREIGN KEY (kode_kabupaten_kota) REFERENCES kabupaten_kota(kode_kabupaten_kota)
        );""",
        metadata={"source": "ddl"},
    ),

    Document(
        page_content="""CREATE TABLE "public"."jumlah_fasilitas_sanitasi_jamban_sehat_permanen_per_kab_kota" (
            "id" int4 NOT NULL DEFAULT nextval('jumlah_fasilitas_sanitasi_jamban_sehat_permanen_per_kab__id_seq'::regclass),
            "kode_kabupaten_kota" int4 NOT NULL,
            "jumlah_fasilitas" int4,
            "satuan" varchar(50) COLLATE "pg_catalog"."default",
            "tahun" int4,
            FOREIGN KEY (kode_kabupaten_kota) REFERENCES kabupaten_kota(kode_kabupaten_kota)
        );""",
        metadata={"source": "ddl"},
    ),

    Document(
        page_content="""CREATE TABLE "public"."jumlah_kk_dengan_akses_sanitasi_layak_per_kab_kota" (
            "id" int4 NOT NULL DEFAULT nextval('jumlah_kk_dengan_akses_sanitasi_layak_per_kab_kota_id_seq'::regclass),
            "kode_kabupaten_kota" int4 NOT NULL,
            "jumlah_kk" int4,
            "satuan" varchar(20) COLLATE "pg_catalog"."default",
            "tahun" int4,
            FOREIGN KEY (kode_kabupaten_kota) REFERENCES kabupaten_kota(kode_kabupaten_kota)
        );""",
        metadata={"source": "ddl"},
    ),

    Document(
        page_content="""CREATE TABLE "public"."jumlah_kk_pengguna_sanitasi_layak_per_kab_kota" (
            "id" int4 NOT NULL DEFAULT nextval('jumlah_kk_pengguna_sanitasi_layak_per_kab_kota_id_seq'::regclass),
            "kode_kabupaten_kota" int4 NOT NULL,
            "jumlah_pengguna" int4,
            "satuan" varchar(20) COLLATE "pg_catalog"."default",
            "tahun" int4,
            FOREIGN KEY (kode_kabupaten_kota) REFERENCES kabupaten_kota(kode_kabupaten_kota)
        );""",
        metadata={"source": "ddl"},
    ),

    Document(
        page_content="""CREATE TABLE "public"."jumlah_nakes_gizi_puskesmas_per_kab_kota" (
            "id" int4 NOT NULL DEFAULT nextval('jumlah_nakes_gizi_puskesmas_per_kab_kota_id_seq'::regclass),
            "kode_kabupaten_kota" int4 NOT NULL,
            "jenis_kelamin" varchar(20) COLLATE "pg_catalog"."default",
            "jumlah_nakes_gizi" int4,
            "satuan" varchar(10) COLLATE "pg_catalog"."default",
            "tahun" int4,
            FOREIGN KEY (kode_kabupaten_kota) REFERENCES kabupaten_kota(kode_kabupaten_kota)
        );""",
        metadata={"source": "ddl"},
    ),

    Document(
        page_content="""CREATE TABLE "public"."jumlah_pemberian_asi_bayi_kurang_6bln_per_kab_kota" (
            "id" int4 NOT NULL DEFAULT nextval('jumlah_pemberian_asi_bayi_kurang_6bln_per_kab_kota_id_seq'::regclass),
            "kode_provinsi" int4,
            "kode_kabupaten_kota" int4,
            "jumlah_bayi" int4,
            "satuan" varchar(10) COLLATE "pg_catalog"."default",
            "tahun" int4,
            FOREIGN KEY (kode_provinsi) REFERENCES provinsi(kode_provinsi),
            FOREIGN KEY (kode_kabupaten_kota) REFERENCES kabupaten_kota(kode_kabupaten_kota)
        );""",
        metadata={"source": "ddl"},
    ),

    Document(
        page_content="""CREATE TABLE "public"."jumlah_penduduk_berdasarkan_kelompok_umur_dan_gender_provinsi" (
            "id" int4 NOT NULL DEFAULT nextval('jumlah_penduduk_berdasarkan_kelompok_umur_dan_gender_pro_id_seq'::regclass),
            "kode_provinsi" int4 NOT NULL,
            "kelompok_umur" varchar(10) COLLATE "pg_catalog"."default" NOT NULL,
            "jumlah_penduduk_pria" int4,
            "jumlah_penduduk_wanita" int4,
            "jumlah_penduduk_pria_dan_wanita" int4,
            "tahun" int4,
            FOREIGN KEY (kode_provinsi) REFERENCES provinsi(kode_provinsi)
        );""",
        metadata={"source": "ddl"},
    ),

    Document(
        page_content="""CREATE TABLE "public"."jumlah_penduduk_miskin_per_kab_kota" (
            "id" int4 NOT NULL DEFAULT nextval('jumlah_penduduk_miskin_per_kabupaten_kota_id_seq'::regclass),
            "kode_kabupaten_kota" int4 NOT NULL,
            "jumlah_penduduk_miskin" int8,
            "satuan" varchar(50) COLLATE "pg_catalog"."default",
            "tahun" int4,
            FOREIGN KEY (kode_kabupaten_kota) REFERENCES kabupaten_kota(kode_kabupaten_kota)
        );""",
        metadata={"source": "ddl"},
    ),

    Document(
        page_content="""CREATE TABLE "public"."jumlah_penduduk_miskin_per_semester_provinsi" (
            "id" int4 NOT NULL DEFAULT nextval('jumlah_penduduk_miskin_per_semester_provinsi_id_seq'::regclass),
            "kode_provinsi" int4 NOT NULL,
            "semester" varchar(50) COLLATE "pg_catalog"."default" NOT NULL,
            "jumlah_penduduk_miskin" int8,
            "satuan" varchar(50) COLLATE "pg_catalog"."default",
            "tahun" int4,
            FOREIGN KEY (kode_provinsi) REFERENCES provinsi(kode_provinsi)
        );""",
        metadata={"source": "ddl"},
    ),

    Document(
        page_content="""CREATE TABLE "public"."jumlah_perkawinan_usia_muda_16_sampai_19_tahun_per_gender" (
            "id" int4 NOT NULL DEFAULT nextval('jumlah_perkawinan_usia_muda_16_sampai_19_tahun_per_gende_id_seq'::regclass),
            "kode_provinsi" int4,
            "kode_kabupaten_kota" int4,
            "jenis_kelamin" varchar(10) COLLATE "pg_catalog"."default",
            "jumlah_perkawinan" int4,
            "satuan" varchar(50) COLLATE "pg_catalog"."default",
            "tahun" int4,
            FOREIGN KEY (kode_provinsi) REFERENCES provinsi(kode_provinsi),
            FOREIGN KEY (kode_kabupaten_kota) REFERENCES kabupaten_kota(kode_kabupaten_kota)
        );""",
        metadata={"source": "ddl"},
    ),

    Document(
        page_content="""CREATE TABLE "public"."jumlah_puskesmas_melaksanakan_keg_kesehatan_remaja_per_kab_kota" (
            "id" int4 NOT NULL DEFAULT nextval('jumlah_puskesmas_melaksanakan_keg_kesehatan_remaja_per_k_id_seq'::regclass),
            "kode_kabupaten_kota" int4 NOT NULL,
            "jumlah_puskesmas" int4,
            "satuan" varchar(15) COLLATE "pg_catalog"."default",
            "tahun" int4,
            FOREIGN KEY (kode_kabupaten_kota) REFERENCES kabupaten_kota(kode_kabupaten_kota)
        );""",
        metadata={"source": "ddl"},
    ),

    Document(
        page_content="""CREATE TABLE "public"."jumlah_puskesmas_melaksanakan_kelas_bumil_per_kab_kota" (
            "id" int4 NOT NULL DEFAULT nextval('jumlah_puskesmas_melaksanakan_kelas_bumil_per_kab_kota_id_seq'::regclass),
            "kode_kabupaten_kota" int4 NOT NULL,
            "jumlah_puskesmas" int4,
            "satuan" varchar(15) COLLATE "pg_catalog"."default",
            "tahun" int4,
            FOREIGN KEY (kode_kabupaten_kota) REFERENCES kabupaten_kota(kode_kabupaten_kota)
        );""",
        metadata={"source": "ddl"},
    ),

    Document(
        page_content="""CREATE TABLE "public"."jumlah_puskesmas_per_kab_kota" (
            "id" int4 NOT NULL DEFAULT nextval('jumlah_puskesmas_per_kab_kota_id_seq'::regclass),
            "kode_kabupaten_kota" int4 NOT NULL,
            "jumlah_puskesmas" int4,
            "satuan" varchar(10) COLLATE "pg_catalog"."default",
            "tahun" int4,
            FOREIGN KEY (kode_kabupaten_kota) REFERENCES kabupaten_kota(kode_kabupaten_kota)
        );""",
        metadata={"source": "ddl"},
    ),

    Document(
        page_content="""CREATE TABLE "public"."jumlah_realisasi_konvergensi_bumil_per_desa" (
            "id" int4 NOT NULL DEFAULT nextval('jumlah_realisasi_konvergensi_bumil_per_desa_id_seq'::regclass),
            "kode_kabupaten_kota" int4 NOT NULL,
            "bps_kode_kecamatan" int8,
            "bps_nama_kecamatan" varchar(255) COLLATE "pg_catalog"."default",
            "bps_kode_desa_kelurahan" int8,
            "bps_nama_desa_kelurahan" varchar(255) COLLATE "pg_catalog"."default",
            "kemendagri_kode_kecamatan" varchar(20) COLLATE "pg_catalog"."default",
            "kemendagri_nama_kecamatan" varchar(255) COLLATE "pg_catalog"."default",
            "kemendagri_kode_desa_kelurahan" varchar(20) COLLATE "pg_catalog"."default",
            "kemendagri_nama_desa_kelurahan" varchar(255) COLLATE "pg_catalog"."default",
            "jumlah_realisasi_konvergensi_ibu_hamil" int4,
            "satuan" varchar(10) COLLATE "pg_catalog"."default",
            "tahun" int4,
            FOREIGN KEY (kode_kabupaten_kota) REFERENCES kabupaten_kota(kode_kabupaten_kota)
        );""",
        metadata={"source": "ddl"},
    ),

    Document(
        page_content="""CREATE TABLE "public"."jumlah_remaja_putri_anemia_per_kab_kota" (
            "id" int4 NOT NULL DEFAULT nextval('jumlah_remaja_putri_anemia_per_kab_kota_id_seq'::regclass),
            "kode_kabupaten_kota" int4 NOT NULL,
            "jumlah_remaja_putri_anemia" int4,
            "satuan" varchar(50) COLLATE "pg_catalog"."default",
            "periode" varchar(50) COLLATE "pg_catalog"."default",
            "tahun" int4,
            FOREIGN KEY (kode_kabupaten_kota) REFERENCES kabupaten_kota(kode_kabupaten_kota)
        );""",
        metadata={"source": "ddl"},
    ),

    Document(
        page_content="""CREATE TABLE "public"."jumlah_remaja_putri_anemia_per_puskesmas" (
            "kode_kabupaten_kota" int4,
            "nama_kabupaten_kota" varchar(255) COLLATE "pg_catalog"."default",
            "bps_kode_kecamatan" int4,
            "bps_nama_kecamatan" varchar(255) COLLATE "pg_catalog"."default",
            "kemendagri_kode_kecamatan" varchar(255) COLLATE "pg_catalog"."default",
            "kemendagri_nama_kecamatan" varchar(255) COLLATE "pg_catalog"."default",
            "kode_puskesmas" varchar(255) COLLATE "pg_catalog"."default",
            "nama_puskesmas" varchar(255) COLLATE "pg_catalog"."default",
            "anemia_smp7" int4,
            "anemia_sma10" int4,
            "satuan" varchar(255) COLLATE "pg_catalog"."default",
            "periode" varchar(255) COLLATE "pg_catalog"."default",
            "tahun" int4
        );""",
        metadata={"source": "ddl"},
    ),

    Document(
        page_content="""CREATE TABLE "public"."jumlah_remaja_putri_per_triwulan_per_kab_kota" (
            "kode_kabupaten_kota" int4,
            "jumlah_remaja_putri" int8,
            "satuan" varchar(255) COLLATE "pg_catalog"."default",
            "triwulan" int4,
            "tahun" int4,
            FOREIGN KEY (kode_kabupaten_kota) REFERENCES kabupaten_kota(kode_kabupaten_kota)
        );""",
        metadata={"source": "ddl"},
    ),

    Document(
        page_content="""CREATE TABLE "public"."jumlah_sarana_sanitasi_jamban_sehat_semipermanen_per_kab_kot" (
            "id" int4 NOT NULL DEFAULT nextval('jumlah_fasilitas_sanitasi_jamban_sehat_semipermanen_per__id_seq'::regclass),
            "kode_kabupaten_kota" int4 NOT NULL,
            "jumlah_sarana" int4,
            "satuan" varchar(10) COLLATE "pg_catalog"."default",
            "tahun" int4,
            FOREIGN KEY (kode_kabupaten_kota) REFERENCES kabupaten_kota(kode_kabupaten_kota)
        );""",
        metadata={"source": "ddl"},
    ),

    Document(
        page_content="""CREATE TABLE "public"."jumlah_sasaran_balita_diukur_per_kab_kota" (
            "id" int4 NOT NULL DEFAULT nextval('jumlah_sasaran_balita_diukur_per_kab_kota_id_seq'::regclass),
            "kode_kabupaten_kota" int4 NOT NULL,
            "jumlah_sasaran_balita" int4,
            "satuan" varchar(50) COLLATE "pg_catalog"."default",
            "tahun" int4,
            FOREIGN KEY (kode_kabupaten_kota) REFERENCES kabupaten_kota(kode_kabupaten_kota)
        );""",
        metadata={"source": "ddl"},
    ),

    Document(
        page_content="""CREATE TABLE "public"."jumlah_sasaran_balita_per_desa" (
            "kode_kabupaten_kota" int4,
            "nama_kabupaten_kota" varchar(255) COLLATE "pg_catalog"."default",
            "bps_kode_kecamatan" int4,
            "bps_nama_kecamatan" varchar(255) COLLATE "pg_catalog"."default",
            "bps_kode_desa_kelurahan" int8,
            "bps_nama_desa_kelurahan" varchar(255) COLLATE "pg_catalog"."default",
            "kemendagri_kode_kecamatan" varchar(255) COLLATE "pg_catalog"."default",
            "kemendagri_nama_kecamatan" varchar(255) COLLATE "pg_catalog"."default",
            "kemendagri_kode_desa_kelurahan" varchar(255) COLLATE "pg_catalog"."default",
            "kemendagri_nama_desa_kelurahan" varchar(255) COLLATE "pg_catalog"."default",
            "kode_puskesmas" varchar(255) COLLATE "pg_catalog"."default",
            "nama_puskesmas" varchar(255) COLLATE "pg_catalog"."default",
            "nama_posyandu" varchar(255) COLLATE "pg_catalog"."default",
            "jumlah_sasaran_anak" int4,
            "satuan" varchar(255) COLLATE "pg_catalog"."default",
            "periode" varchar(255) COLLATE "pg_catalog"."default",
            "tahun" int4
        );""",
        metadata={"source": "ddl"},
    ),

    Document(
        page_content="""CREATE TABLE "public"."jumlah_sasaran_bumil_per_kab_kota" (
            "kode_kabupaten_kota" int4,
            "nama_kabupaten_kota" varchar(255) COLLATE "pg_catalog"."default",
            "jumlah_bumil_anemia" int4,
            "satuan" varchar(255) COLLATE "pg_catalog"."default",
            "periode" varchar(255) COLLATE "pg_catalog"."default",
            "tahun" int4,
            FOREIGN KEY (kode_kabupaten_kota) REFERENCES kabupaten_kota(kode_kabupaten_kota)
        );""",
        metadata={"source": "ddl"},
    ),

    Document(
        page_content="""CREATE TABLE "public"."jumlah_sasaran_bumil_per_puskesmas" (
            "kode_kabupaten_kota" int4,
            "nama_kabupaten_kota" varchar(255) COLLATE "pg_catalog"."default",
            "bps_kode_kecamatan" int4,
            "bps_nama_kecamatan" varchar(255) COLLATE "pg_catalog"."default",
            "kemendagri_kode_kecamatan" varchar(255) COLLATE "pg_catalog"."default",
            "kemendagri_nama_kecamatan" varchar(255) COLLATE "pg_catalog"."default",
            "kode_puskesmas" varchar(255) COLLATE "pg_catalog"."default",
            "nama_puskesmas" varchar(255) COLLATE "pg_catalog"."default",
            "bumil_sampai_bulan_ini" int4,
            "satuan" varchar(255) COLLATE "pg_catalog"."default",
            "periode" varchar(255) COLLATE "pg_catalog"."default",
            "tahun" int4
        );""",
        metadata={"source": "ddl"},
    ),

    Document(
        page_content="""CREATE TABLE "public"."jumlah_sasaran_individu_calon_pengantin_diperiksa_per_kab_kota" (
            "id" int4 NOT NULL DEFAULT nextval('jumlah_sasaran_individu_calon_pengantin_diperiksa_per_ka_id_seq'::regclass),
            "kode_kabupaten_kota" int4 NOT NULL,
            "jumlah_individu_catin" int4,
            "satuan" varchar(50) COLLATE "pg_catalog"."default",
            "tahun" int4,
            FOREIGN KEY (kode_kabupaten_kota) REFERENCES kabupaten_kota(kode_kabupaten_kota)
        );""",
        metadata={"source": "ddl"},
    ),

    Document(
        page_content="""CREATE TABLE "public"."jumlah_sasaran_keluarga_per_desa" (
            "kode bps" int4,
            "nama_kabupaten_kota" varchar(255) COLLATE "pg_catalog"."default",
            "bps_kode_kecamatan" int4,
            "bps_nama_kecamatan" varchar(255) COLLATE "pg_catalog"."default",
            "bps_kode_desa_kelurahan" int8,
            "nama_desa_kelurahan" varchar(255) COLLATE "pg_catalog"."default",
            "kemendagri_kode_kecamatan" varchar(255) COLLATE "pg_catalog"."default",
            "kemendagri_nama_kecamatan" varchar(255) COLLATE "pg_catalog"."default",
            "kemendagri_kode_desa_kelurahan" varchar(255) COLLATE "pg_catalog"."default",
            "kemendagri_desa_kelurahan" varchar(255) COLLATE "pg_catalog"."default",
            "jumlah_keluarga_sasaran" int4,
            "satuan" varchar(255) COLLATE "pg_catalog"."default",
            "tahun" int4
        );""",
        metadata={"source": "ddl"},
    ),

    Document(
        page_content="""CREATE TABLE "public"."jumlah_sasaran_konvergensi_bumil_per_desa" (
            "id" int4 NOT NULL DEFAULT nextval('jumlah_sasaran_konvergensi_bumil_per_desa_id_seq'::regclass),
            "kode_kabupaten_kota" int4 NOT NULL,
            "bps_kode_kecamatan" int8,
            "bps_nama_kecamatan" varchar(255) COLLATE "pg_catalog"."default",
            "bps_kode_desa_kelurahan" int8,
            "bps_nama_desa_kelurahan" varchar(255) COLLATE "pg_catalog"."default",
            "kemendagri_kode_kecamatan" varchar(20) COLLATE "pg_catalog"."default",
            "kemendagri_nama_kecamatan" varchar(255) COLLATE "pg_catalog"."default",
            "kemendagri_kode_desa_kelurahan" varchar(20) COLLATE "pg_catalog"."default",
            "kemendagri_nama_desa_kelurahan" varchar(255) COLLATE "pg_catalog"."default",
            "jumlah_sasaran_konvergensi_ibu_hamil" int4,
            "satuan" varchar(10) COLLATE "pg_catalog"."default",
            "tahun" int4,
            FOREIGN KEY (kode_kabupaten_kota) REFERENCES kabupaten_kota(kode_kabupaten_kota)
        );""",
        metadata={"source": "ddl"},
    ),

    Document(
        page_content="""CREATE TABLE "public"."jumlah_sasaran_pasangan_calon_pengantin_diperiksa_per_kab_kota" (
            "id" int4 NOT NULL DEFAULT nextval('jumlah_sasaran_pasangan_calon_pengantin_diperiksa_per_ka_id_seq'::regclass),
            "kode_kabupaten_kota" int4 NOT NULL,
            "jumlah_pasangan_catin" int4,
            "satuan" varchar(50) COLLATE "pg_catalog"."default",
            "tahun" int4,
            FOREIGN KEY (kode_kabupaten_kota) REFERENCES kabupaten_kota(kode_kabupaten_kota)
        );""",
        metadata={"source": "ddl"},
    ),

    Document(
        page_content="""CREATE TABLE "public"."jumlah_sasaran_remaja_putri_per_puskesmas" (
            "kode_kabupaten_kota" int4,
            "nama_kabupaten_kota" varchar(255) COLLATE "pg_catalog"."default",
            "bps_kode_kecamatan" int4,
            "bps_nama_kecamatan" varchar(255) COLLATE "pg_catalog"."default",
            "kemendagri_kode_kecamatan" varchar(255) COLLATE "pg_catalog"."default",
            "kemendagri_nama_kecamatan" varchar(255) COLLATE "pg_catalog"."default",
            "kode_puskesmas" varchar(255) COLLATE "pg_catalog"."default",
            "nama_puskesmas" varchar(255) COLLATE "pg_catalog"."default",
            "jumlah_sasaran_rematri" int4,
            "satuan" varchar(255) COLLATE "pg_catalog"."default",
            "periode" varchar(255) COLLATE "pg_catalog"."default",
            "tahun" int4
        );""",
        metadata={"source": "ddl"},
    ),

    Document(
        page_content="""CREATE TABLE "public"."kabupaten_kota" (
            "kode_kabupaten_kota" int4 NOT NULL,
            "kode_provinsi" int4,
            "nama_kabupaten_kota" varchar(255) COLLATE "pg_catalog"."default" NOT NULL,
            FOREIGN KEY (kode_provinsi) REFERENCES provinsi(kode_provinsi)
        );""",
        metadata={"source": "ddl"},
    ),

    Document(
        page_content="""CREATE TABLE "public"."keluarga_rentan_stunting_per_desa" (
            "kode bps" int4,
            "nama_kabupaten_kota" varchar(255) COLLATE "pg_catalog"."default",
            "bps_kode_kecamatan" int4,
            "bps_nama_kecamatan" varchar(255) COLLATE "pg_catalog"."default",
            "bps_kode_desa_kelurahan" int8,
            "nama_desa_kelurahan" varchar(255) COLLATE "pg_catalog"."default",
            "kemendagri_kode_kecamatan" varchar(255) COLLATE "pg_catalog"."default",
            "kemendagri_nama_kecamatan" varchar(255) COLLATE "pg_catalog"."default",
            "kemendagri_kode_desa_kelurahan" varchar(255) COLLATE "pg_catalog"."default",
            "kemendagri_nama_desa_kelurahan" varchar(255) COLLATE "pg_catalog"."default",
            "jumlah_keluarga_rentan_stunting" int4,
            "satuan" varchar(255) COLLATE "pg_catalog"."default",
            "tahun" int4
        );""",
        metadata={"source": "ddl"},
    ),

    Document(
        page_content="""CREATE TABLE "public"."lokasi_fokus_lokus_per_desa" (
            "kode_kabupaten_kota" int4,
            "nama_kabupaten_kota" varchar(255) COLLATE "pg_catalog"."default",
            "bps_kode_kecamatan" int4,
            "bps_nama_kecamatan" varchar(255) COLLATE "pg_catalog"."default",
            "bps_kode_desa_kelurahan" int8,
            "bps_nama_desa_kelurahan" varchar(255) COLLATE "pg_catalog"."default",
            "kemendagri_kode_kecamatan" varchar(255) COLLATE "pg_catalog"."default",
            "kemendagri_nama_kecamatan" varchar(255) COLLATE "pg_catalog"."default",
            "kemendagri_kode_desa_kelurahan" varchar(255) COLLATE "pg_catalog"."default",
            "kemendagri_nama_desa_kelurahan" varchar(255) COLLATE "pg_catalog"."default",
            "kode_puskesmas" varchar(255) COLLATE "pg_catalog"."default",
            "nama_puskesmas" varchar(255) COLLATE "pg_catalog"."default",
            "status" varchar(255) COLLATE "pg_catalog"."default"
        );""",
        metadata={"source": "ddl"},
    ),

    Document(
        page_content="""CREATE TABLE "public"."persen_balita_bb_kurang_dapat_pmt_per_triwulan_per_kab_kota" (
            "id" int4 NOT NULL DEFAULT nextval('persen_balita_bb_kurang_tambah_gizi_per_triwulan_per_kab_id_seq'::regclass),
            "kode_kabupaten_kota" int4 NOT NULL,
            "persen_balita_bb_kurang_dapat_tambahan_asupan_gizi" numeric(5,2),
            "satuan" varchar(50) COLLATE "pg_catalog"."default",
            "triwulan" int4,
            "tahun" int4,
            FOREIGN KEY (kode_kabupaten_kota) REFERENCES kabupaten_kota(kode_kabupaten_kota)
        );""",
        metadata={"source": "ddl"},
    ),

    Document(
        page_content="""CREATE TABLE "public"."persen_balita_bb_stuck_dapat_pmt_per_triwulan_per_kab_kota" (
            "id" int4 NOT NULL DEFAULT nextval('persen_balita_bb_stuck_tambah_gizi_per_triwulan_per_kab__id_seq'::regclass),
            "kode_kabupaten_kota" int4 NOT NULL,
            "persen_balita_bb_stuck_dapat_tambahan_asupan_gizi" numeric(5,2),
            "satuan" varchar(50) COLLATE "pg_catalog"."default",
            "triwulan" int4,
            "tahun" int4,
            FOREIGN KEY (kode_kabupaten_kota) REFERENCES kabupaten_kota(kode_kabupaten_kota)
        );""",
        metadata={"source": "ddl"},
    ),

    Document(
        page_content="""CREATE TABLE "public"."persen_balita_datang_diukur_bulanan_per_triwulan_per_kab_kota" (
            "id" int4 NOT NULL DEFAULT nextval('persen_balita_datang_diukur_bulanan_per_triwulan_per_kab_id_seq'::regclass),
            "kode_kabupaten_kota" int4 NOT NULL,
            "persentase_ds" numeric(5,2),
            "satuan" varchar(50) COLLATE "pg_catalog"."default",
            "triwulan" int4,
            "tahun" int4,
            FOREIGN KEY (kode_kabupaten_kota) REFERENCES kabupaten_kota(kode_kabupaten_kota)
        );""",
        metadata={"source": "ddl"},
    ),

    Document(
        page_content="""CREATE TABLE "public"."persen_balita_gizi_kurang_dapat_pmt_per_triwulan_per_kab_kota" (
            "id" int4 NOT NULL DEFAULT nextval('persen_balita_gizi_kurang_dapat_pmt_per_triwulan_per_kab_id_seq'::regclass),
            "kode_kabupaten_kota" int4 NOT NULL,
            "persentase_balita_gizi_kurang_dapat_pmt" numeric(5,2),
            "satuan" varchar(50) COLLATE "pg_catalog"."default",
            "triwulan" int4,
            "tahun" int4,
            FOREIGN KEY (kode_kabupaten_kota) REFERENCES kabupaten_kota(kode_kabupaten_kota)
        );""",
        metadata={"source": "ddl"},
    ),

    Document(
        page_content="""CREATE TABLE "public"."persen_bumil_kek_konsumsi_pmt_per_triwulan_per_kab_kota" (
            "id" int4 NOT NULL DEFAULT nextval('persen_bumil_kek_konsum_makan_tambahan_per_triwulan_per__id_seq'::regclass),
            "kode_kabupaten_kota" int4 NOT NULL,
            "persentase_ibu_hamil_kek_yang_mengonsumsi_makanan_tambahan" numeric(5,2),
            "satuan" varchar(50) COLLATE "pg_catalog"."default",
            "triwulan" int4,
            "tahun" int4,
            FOREIGN KEY (kode_kabupaten_kota) REFERENCES kabupaten_kota(kode_kabupaten_kota)
        );""",
        metadata={"source": "ddl"},
    ),

    Document(
        page_content="""CREATE TABLE "public"."persen_bumil_penerima_imunisasi_tetanus_diphtheria_per_kab_kota" (
            "id" int4 NOT NULL DEFAULT nextval('persen_bumil_penerima_imunisasi_tetanus_diphtheria_per_k_id_seq'::regclass),
            "kode_kabupaten_kota" int4 NOT NULL,
            "jenis_imunisasi" varchar(10) COLLATE "pg_catalog"."default",
            "persentase_imunisasi" numeric(5,2),
            "satuan" varchar(10) COLLATE "pg_catalog"."default",
            "tahun" int4,
            FOREIGN KEY (kode_kabupaten_kota) REFERENCES kabupaten_kota(kode_kabupaten_kota)
        );""",
        metadata={"source": "ddl"},
    ),

    Document(
        page_content="""CREATE TABLE "public"."persen_pelayanan_kesehatan_pada_bumil_per_kategori_per_kab_kota" (
            "id" int4 NOT NULL DEFAULT nextval('persen_pelayanan_kesehatan_pada_bumil_per_kategori_per_k_id_seq'::regclass),
            "kode_kabupaten_kota" int4 NOT NULL,
            "jenis_kunjungan" varchar(10) COLLATE "pg_catalog"."default",
            "persentase_kunjungan" numeric(5,2),
            "satuan" varchar(50) COLLATE "pg_catalog"."default",
            "tahun" int4,
            FOREIGN KEY (kode_kabupaten_kota) REFERENCES kabupaten_kota(kode_kabupaten_kota)
        );""",
        metadata={"source": "ddl"},
    ),

    Document(
        page_content="""CREATE TABLE "public"."persen_puskesmas_bisa_laksanagiziburuk_per_triwulan_per_kab_kot" (
            "id" int4 NOT NULL DEFAULT nextval('persen_puskesmas_bisa_laksanagiziburuk_per_triwulan_per__id_seq'::regclass),
            "kode_kabupaten_kota" int4 NOT NULL,
            "persentase_puskesmas_mampu_tatalaksana_gizi_buruk" numeric(5,2),
            "satuan" varchar(50) COLLATE "pg_catalog"."default",
            "triwulan" int4,
            "tahun" int4,
            FOREIGN KEY (kode_kabupaten_kota) REFERENCES kabupaten_kota(kode_kabupaten_kota)
        );""",
        metadata={"source": "ddl"},
    ),

    Document(
        page_content="""CREATE TABLE "public"."persen_remaja_putri_konsumsi_tab_tambah_darah_per_puskesmas" (
            "kode_kabupaten_kota" int4,
            "nama_kabupaten_kota" varchar(255) COLLATE "pg_catalog"."default",
            "bps_kode_kecamatan" int4,
            "bps_nama_kecamatan" varchar(255) COLLATE "pg_catalog"."default",
            "kemendagri_kode_kecamatan" varchar(255) COLLATE "pg_catalog"."default",
            "kemendagri_nama_kecamatan" varchar(255) COLLATE "pg_catalog"."default",
            "kode_puskesmas" varchar(255) COLLATE "pg_catalog"."default",
            "nama_puskesmas" varchar(255) COLLATE "pg_catalog"."default",
            "ttd_persen_konsumsi" float8,
            "satuan" varchar(255) COLLATE "pg_catalog"."default",
            "periode" varchar(255) COLLATE "pg_catalog"."default",
            "tahun" int4
        );""",
        metadata={"source": "ddl"},
    ),

    Document(
        page_content="""CREATE TABLE "public"."persentase_balita_stunting_per_kab_kota" (
            "id" int4 NOT NULL DEFAULT nextval('persentase_balita_stunting_per_kabupaten_kota_id_seq'::regclass),
            "kode_kabupaten_kota" int4 NOT NULL,
            "persentase_balita_stunting" numeric(5,2),
            "satuan" varchar(50) COLLATE "pg_catalog"."default",
            "tahun" int4,
            "periode" varchar(255) COLLATE "pg_catalog"."default",
            FOREIGN KEY (kode_kabupaten_kota) REFERENCES kabupaten_kota(kode_kabupaten_kota)
        );""",
        metadata={"source": "ddl"},
    ),

    Document(
        page_content="""CREATE TABLE "public"."persentase_balita_stunting_per_triwulan_per_kab_kota" (
            "id" int4 NOT NULL DEFAULT nextval('persentase_balita_stunting_per_triwulan_per_kab_kota_id_seq'::regclass),
            "kode_kabupaten_kota" int4 NOT NULL,
            "persentase_balita_stunting" numeric(5,2),
            "satuan" varchar(50) COLLATE "pg_catalog"."default",
            "triwulan" int4,
            "tahun" int4,
            FOREIGN KEY (kode_kabupaten_kota) REFERENCES kabupaten_kota(kode_kabupaten_kota)
        );""",
        metadata={"source": "ddl"},
    ),

    Document(
        page_content="""CREATE TABLE "public"."persentase_bayi_dapat_asi_per_puskesmas" (
            "kode_kabupaten_kota" int4,
            "nama_kabupaten_kota" varchar(255) COLLATE "pg_catalog"."default",
            "bps_kode_kecamatan" int4,
            "bps_nama_kecamatan" varchar(255) COLLATE "pg_catalog"."default",
            "kemendagri_kode_kecamatan" varchar(255) COLLATE "pg_catalog"."default",
            "kemendagri_nama_kecamatan" varchar(255) COLLATE "pg_catalog"."default",
            "kode_puskesmas" varchar(255) COLLATE "pg_catalog"."default",
            "nama_puskesmas" varchar(255) COLLATE "pg_catalog"."default",
            "asi_6bln_jml_bayi_usia_6bln" int4,
            "asi_6bln_jml_bayi_asi_eksklusif" int4,
            "asi_6bln_pct" float8,
            "satuan" varchar(255) COLLATE "pg_catalog"."default",
            "periode" varchar(255) COLLATE "pg_catalog"."default",
            "tahun" int4
        );""",
        metadata={"source": "ddl"},
    ),

    Document(
        page_content="""CREATE TABLE "public"."persentase_bayi_dapat_mpasi_beragam_per_puskesmas" (
            "kode_kabupaten_kota" int4,
            "nama_kabupaten_kota" varchar(255) COLLATE "pg_catalog"."default",
            "bps_kode_kecamatan" int4,
            "bps_nama_kecamatan" varchar(255) COLLATE "pg_catalog"."default",
            "kemendagri_kode_kecamatan" varchar(255) COLLATE "pg_catalog"."default",
            "kemendagri_nama_kecamatan" varchar(255) COLLATE "pg_catalog"."default",
            "kode_puskesmas" varchar(255) COLLATE "pg_catalog"."default",
            "nama_puskesmas" varchar(255) COLLATE "pg_catalog"."default",
            "mpasi_pct_6_23bln_beragam" float8,
            "satuan" varchar(255) COLLATE "pg_catalog"."default",
            "periode" varchar(255) COLLATE "pg_catalog"."default",
            "tahun" int4
        );""",
        metadata={"source": "ddl"},
    ),

    Document(
        page_content="""CREATE TABLE "public"."persentase_bumil_kek_dapat_pmt_per_triwulan_per_kab_kota" (
            "id" int4 NOT NULL DEFAULT nextval('persentase_bumil_kek_dapat_asupan_gizi_per_triwulan_per__id_seq'::regclass),
            "kode_kabupaten_kota" int4 NOT NULL,
            "persentase_ibu_hamil_kek_yang_mendapat_makanan_tambahan" numeric(5,2),
            "satuan" varchar(50) COLLATE "pg_catalog"."default",
            "triwulan" int4,
            "tahun" int4,
            FOREIGN KEY (kode_kabupaten_kota) REFERENCES kabupaten_kota(kode_kabupaten_kota)
        );""",
        metadata={"source": "ddl"},
    ),

    Document(
        page_content="""CREATE TABLE "public"."persentase_bumil_kurang_energi_kronis_per_puskesmas" (
            "kode_kabupaten_kota" int4,
            "nama_kabupaten_kota" varchar(255) COLLATE "pg_catalog"."default",
            "bps_kode_kecamatan" int4,
            "bps_nama_kecamatan" varchar(255) COLLATE "pg_catalog"."default",
            "kemendagri_kode_kecamatan" varchar(255) COLLATE "pg_catalog"."default",
            "kemendagri_nama_kecamatan" varchar(255) COLLATE "pg_catalog"."default",
            "kode_puskesmas" varchar(255) COLLATE "pg_catalog"."default",
            "nama_puskesmas" varchar(255) COLLATE "pg_catalog"."default",
            "ibu_hamil_persen_kek" float8,
            "satuan" varchar(255) COLLATE "pg_catalog"."default",
            "periode" varchar(255) COLLATE "pg_catalog"."default",
            "tahun" int4
        );""",
        metadata={"source": "ddl"},
    ),

    Document(
        page_content="""CREATE TABLE "public"."persentase_bumil_kurang_energi_kronis_per_triwulan_per_kab_kota" (
            "id" int4 NOT NULL DEFAULT nextval('persentase_bumil_kurang_energi_kronis_per_triwulan_per_k_id_seq'::regclass),
            "kode_kabupaten_kota" int4 NOT NULL,
            "persentase_ibu_hamil_kek" numeric(5,2),
            "satuan" varchar(50) COLLATE "pg_catalog"."default",
            "triwulan" int4,
            "tahun" int4,
            FOREIGN KEY (kode_kabupaten_kota) REFERENCES kabupaten_kota(kode_kabupaten_kota)
        );""",
        metadata={"source": "ddl"},
    ),

    Document(
        page_content="""CREATE TABLE "public"."persentase_bumil_penerima_tab_tambah_darah_per_kab_kota" (
            "id" int4 NOT NULL DEFAULT nextval('persentase_bumil_penerima_tab_tambah_darah_per_kab_kota_id_seq'::regclass),
            "kode_kabupaten_kota" int4 NOT NULL,
            "persentase_penerima" numeric(5,2),
            "satuan" varchar(50) COLLATE "pg_catalog"."default",
            "tahun" int4,
            FOREIGN KEY (kode_kabupaten_kota) REFERENCES kabupaten_kota(kode_kabupaten_kota)
        );""",
        metadata={"source": "ddl"},
    ),

    Document(
        page_content="""CREATE TABLE "public"."persentase_keluarga_dengan_akses_sanitasi_layak_per_kab_kota" (
            "id" int4 NOT NULL DEFAULT nextval('persentase_keluarga_dengan_akses_sanitasi_layak_per_kab__id_seq'::regclass),
            "kode_kabupaten_kota" int4 NOT NULL,
            "persentase_sanitasi_layak" numeric(5,2),
            "satuan" varchar(20) COLLATE "pg_catalog"."default",
            "tahun" int4,
            FOREIGN KEY (kode_kabupaten_kota) REFERENCES kabupaten_kota(kode_kabupaten_kota)
        );""",
        metadata={"source": "ddl"},
    ),

    Document(
        page_content="""CREATE TABLE "public"."persentase_pemberian_asi_bayi_kurang_6bln_per_kab_kota" (
            "id" int4 NOT NULL DEFAULT nextval('persentase_pemberian_asi_bayi_kurang_6bln_per_kabupaten__id_seq'::regclass),
            "kode_kabupaten_kota" int4 NOT NULL,
            "persentase_pemberian_asi" numeric(5,2),
            "satuan" varchar(50) COLLATE "pg_catalog"."default",
            "tahun" int4,
            FOREIGN KEY (kode_kabupaten_kota) REFERENCES kabupaten_kota(kode_kabupaten_kota)
        );""",
        metadata={"source": "ddl"},
    ),

    Document(
        page_content="""CREATE TABLE "public"."persentase_penduduk_miskin_per_kab_kota" (
            "id" int4 NOT NULL DEFAULT nextval('persentase_penduduk_miskin_per_kabupaten_kota_id_seq'::regclass),
            "kode_kabupaten_kota" int4 NOT NULL,
            "persentase_penduduk_miskin" numeric(5,2),
            "satuan" varchar(50) COLLATE "pg_catalog"."default",
            "tahun" int4,
            FOREIGN KEY (kode_kabupaten_kota) REFERENCES kabupaten_kota(kode_kabupaten_kota)
        );""",
        metadata={"source": "ddl"},
    ),

    Document(
        page_content="""CREATE TABLE "public"."persentase_penduduk_miskin_per_semester_provinsi" (
            "id" int4 NOT NULL DEFAULT nextval('persentase_penduduk_miskin_per_semester_provinsi_id_seq'::regclass),
            "kode_provinsi" int4 NOT NULL,
            "semester" varchar(20) COLLATE "pg_catalog"."default" NOT NULL,
            "persentase_penduduk_miskin" numeric(5,2),
            "satuan" varchar(20) COLLATE "pg_catalog"."default",
            "tahun" int4,
            FOREIGN KEY (kode_provinsi) REFERENCES provinsi(kode_provinsi)
        );""",
        metadata={"source": "ddl"},
    ),

    Document(
        page_content="""CREATE TABLE "public"."persentase_penduduk_miskin_provinsi" (
            "id" int4 NOT NULL DEFAULT nextval('persentase_penduduk_miskin_provinsi_id_seq'::regclass),
            "kode_provinsi" int4 NOT NULL,
            "persentase_penduduk_miskin" numeric(5,2),
            "satuan" varchar(50) COLLATE "pg_catalog"."default",
            "tahun" int4,
            FOREIGN KEY (kode_provinsi) REFERENCES provinsi(kode_provinsi)
        );""",
        metadata={"source": "ddl"},
    ),

    Document(
        page_content="""CREATE TABLE "public"."persentase_puskesmas_tersedia_obat_vaksin_esensial_per_kab_kota" (
            "id" int4 NOT NULL DEFAULT nextval('persentase_puskesmas_tersedia_obat_vaksin_esensial_per_k_id_seq'::regclass),
            "kode_kabupaten_kota" int4 NOT NULL,
            "persentase_cakupan_puskesmas" numeric(5,2),
            "satuan" varchar(10) COLLATE "pg_catalog"."default",
            "tahun" int4,
            FOREIGN KEY (kode_kabupaten_kota) REFERENCES kabupaten_kota(kode_kabupaten_kota)
        );""",
        metadata={"source": "ddl"},
    ),

    Document(
        page_content="""CREATE TABLE "public"."prevalensi_balita_stunting_per_kab_kota" (
            "id" int4 NOT NULL DEFAULT nextval('prevalensi_balita_stunting_per_kab_kota_id_seq'::regclass),
            "kode_kabupaten_kota" int4 NOT NULL,
            "prevalensi_balita_stunting" numeric(5,2),
            "satuan" varchar(50) COLLATE "pg_catalog"."default",
            "tahun" int4,
            "sumber" varchar(255) COLLATE "pg_catalog"."default",
            FOREIGN KEY (kode_kabupaten_kota) REFERENCES kabupaten_kota(kode_kabupaten_kota)
        );""",
        metadata={"source": "ddl"},
    ),

    Document(
        page_content="""CREATE TABLE "public"."prevalensi_balita_stunting_per_provinsi" (
            "id" int4 NOT NULL DEFAULT nextval('prevalensi_balita_stunting_per_kab_kota_id_seq'::regclass),
            "kode_provinsi" int4 NOT NULL,
            "prevalensi_balita_stunting" numeric(5,2),
            "satuan" varchar(50) COLLATE "pg_catalog"."default",
            "tahun" int4,
            FOREIGN KEY (kode_provinsi) REFERENCES provinsi(kode_provinsi)
        );""",
        metadata={"source": "ddl"},
    ),

    Document(
        page_content="""CREATE TABLE "public"."program_kegiatan_realisasi_anggaran_stunting_per_opd" (
            "id" int4 NOT NULL DEFAULT nextval('program_kegiatan_anggaran_realisasi_organisasi_perangkat_id_seq'::regclass),
            "kode_provinsi" int4,
            "organisasi_perangkat_daerah" varchar(255) COLLATE "pg_catalog"."default",
            "program" text COLLATE "pg_catalog"."default",
            "kegiatan" text COLLATE "pg_catalog"."default",
            "jumlah_anggaran" int8,
            "jumlah_realisasi" int8,
            "tahun" int4,
            FOREIGN KEY (kode_provinsi) REFERENCES provinsi(kode_provinsi)
        );""",
        metadata={"source": "ddl"},
    ),

    Document(
        page_content="""CREATE TABLE "public"."provinsi" (
            "kode_provinsi" int4 NOT NULL,
            "nama_provinsi" varchar(255) COLLATE "pg_catalog"."default" NOT NULL
        );""",
        metadata={"source": "ddl"},
    ),

    Document(
        page_content="""CREATE TABLE "public"."rata_rata_lama_sekolah_per_kab_kota" (
            "id" int4 NOT NULL DEFAULT nextval('rata_rata_lama_sekolah_per_kab_kota_id_seq'::regclass),
            "kode_kabupaten_kota" int4 NOT NULL,
            "rata_rata_lama_sekolah" numeric(5,2),
            "satuan" varchar(10) COLLATE "pg_catalog"."default",
            "tahun" int4,
            FOREIGN KEY (kode_kabupaten_kota) REFERENCES kabupaten_kota(kode_kabupaten_kota)
        );""",
        metadata={"source": "ddl"},
    ),

    Document(
        page_content="""CREATE TABLE "public"."rata_rata_lama_sekolah_per_provinsi" (
            "id" int4 NOT NULL DEFAULT nextval('rata_rata_lama_sekolah_per_provinsi_id_seq'::regclass),
            "kode_provinsi" int4 NOT NULL,
            "rata_rata_lama_sekolah" numeric(5,2),
            "satuan" varchar(10) COLLATE "pg_catalog"."default",
            "tahun" int4,
            FOREIGN KEY (kode_provinsi) REFERENCES provinsi(kode_provinsi)
        );""",
        metadata={"source": "ddl"},
    ),

]


# Generate UUIDs untuk setiap dokumen
ddl_uuids = [str(uuid4()) for _ in range(len(ddl_documents))]
